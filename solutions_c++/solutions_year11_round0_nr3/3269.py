#include<iostream>
#include<conio.h>
#include<stdio.h>
#include<fstream>
#include<string>
#include<algorithm>

using namespace std ;

unsigned long int x=0,pos=0,k=0,n=0,t=0,numarr[100],arr1[100],arr2[100],checkArray[100],truesum1,truesum2,maxi;
int binaryArr[100][100],sum[100],fsum[100],sum1[100],sum2[100];
char arr[500000];
float moves;

void get_file();
void readt();
void readn();
void get_array();
bool isComplete();
void defineCheckArray();
void defineBinaryArray();
void addOne(int posx);
void convertToBinary(int posx);
void defineSum();
void checkTrueSum();
void checkFalseSum();
void printSum();
void printfSum();
void patrickAdd(int *s,int *ba);
void getTrueSum1();
void getTrueSum2();
bool checkEquality();

void main()
{
	get_file();
	readt();
	for(int ii=0;ii<t;ii++)
	{
		maxi=0;
		readn();
		get_array();
		/*cout << "\nT=" <<t<< " N=" <<n;
		cout << "\nArray : ";
		for(int jj=1;jj<=n;jj++)
			cout << numarr[jj] << " ";
		getch();*/
		defineCheckArray();
		defineBinaryArray();
		for(int jj=1;jj<=n;jj++)
			convertToBinary(jj);
		addOne(n);
		while (isComplete() != true)
		{
			checkTrueSum();
			
			
			for(int jj =0;jj<=32;jj++)
				sum1[jj] =  sum[jj];
			
			
			checkFalseSum();
			
			for(int jj =0;jj<=32;jj++)
				sum2[jj]= fsum[jj];



			/*cout << "\n\tAfter  SUM = ";
			for(int jj =0;jj<=32;jj++)
				cout << sum1[jj];
			cout << "\n";
			cout << "\n\tAfter fSUM = ";
			for(int jj =0;jj<=32;jj++)
				cout << sum2[jj];
			cout << "\n";*/
			
			
			bool isEqual = checkEquality();
			if(isEqual == true){
				getTrueSum1();
				getTrueSum2();
				int temp = truesum1>truesum2?truesum1:truesum2;
				maxi = maxi>temp?maxi:temp;
				//cout << "\nTrue Sum1 = " <<truesum1;
				//cout << "\nTrue Sum2 = " <<truesum2;
			}
			/*cout << "\n\t1Check Array : ";
			for(int ii=0;ii<=n;ii++)
				cout << checkArray[ii];
			getch();*/
			addOne(n);
		}
		//cout << "\n\n\t\tMAX = " << maxi;
		FILE *fout;
		fout =fopen("output.in","a+");
		if(maxi == 0)
			fprintf(fout,"Case #%d: NO\n",(ii+1));
		else
			fprintf(fout,"Case #%d: %d\n",(ii+1),maxi);
		fclose(fout);

	}
}

void get_file()
{
	ifstream fin;
	fin.open("input.in" , ios :: in);
	while(fin)
	{
		fin.get(arr[x]);
		x++;
	}
	fin.close();
}

void readt()
{
	while (arr[pos] != '\n')
	{
		t =  (t*10) + (arr[pos] - 48);
		pos++;
	}
}

void readn()
{
	n=0;
	pos++;
	while (arr[pos] != '\n')
	{
		n = (n*10) + ( arr[pos] - 48 );
		pos++;
	}
}

void get_array()
{
	for(int ii =1;ii<=n;ii++)
	{
		pos++;
		numarr[ii]=0;
		while (arr[pos] != ' ' && arr[pos] != '\n' && arr[pos] != '\0')
		{
			numarr[ii] = (numarr[ii]*10) + ( arr[pos] - 48 );
			pos++;
		}
	}
}

bool isComplete()
{
	for(int ii =1;ii<=n;ii++)
	{
		if(checkArray[ii] == 0)
			return false;
	}
	return true;
}

void defineCheckArray()
{
	for(int ii=0;ii<n+1;ii++)
		checkArray[ii]=0;
}

void defineBinaryArray()
{
	for(int jj=0;jj<100;jj++)
		for(int ii=0;ii<=32;ii++)
			binaryArr[jj][ii]=0;
}

void addOne(int posx)
{
	checkArray[posx]++;
	if(checkArray[posx] == 2)
	{checkArray[posx] = 0;addOne(posx-1);}
	
}

void convertToBinary(int posx)
{
	unsigned int temp = numarr[posx];
	int count=0;
	while(temp >0)
	{
		binaryArr[posx][32-count] = temp%2;
		count++;
		temp=temp/2;
	}
	/*
	cout << "\nBINARY : ";
	for(int ii=0;ii<=32;ii++)
		cout <<binaryArr[posx][ii];
	getch();*/
}

void checkTrueSum()
{
	defineSum();
	for(int ii = 1; ii<=n;ii++)
	{
		//cout << "\nCHECKING TRUE SUM";
		if(checkArray[ii] == 1)
			patrickAdd(sum,binaryArr[ii]);
	}
	
}
void checkFalseSum()
{
	defineSum();
	for(int ii = 1; ii<=n;ii++)
	{
		if(checkArray[ii] == 0)
			patrickAdd(fsum,binaryArr[ii]);
	}
	
}
void defineSum()
{
	for(int ii=0;ii<33;ii++)
	{sum[ii]=0;fsum[ii]=0;}
}

void patrickAdd(int *s,int *ba)
{
	/*cout << "\nAdding ";
	for(int jj =0;jj<=32;jj++)
			cout << s[jj];
	cout << "\nAnd    ";
	for(int jj =0;jj<=32;jj++)
			cout << ba[jj];*/
	//cout << "\n\t Patrick Add : \n";
	//bool carry = false;
	for(int ii=32;ii>=0;ii--)
	{
		/*for(int jj =0;jj<=32;jj++)
			cout << s[jj];
		cout << "\n";*/
		/*if(carry == true)
		{
			s[ii]++;
			carry = false;
			if(s[ii] >= 2)
			{s[ii] =0;carry = true;}
		}*/
		s[ii] = s[ii] + ba[ii];
		if(s[ii] >= 2)
		{
			s[ii]=0;
			//carry=true;
		}
	}
	//getch();
	
}

void printSum()
{
	cout << "\nSUM  = ";
	for(int ii=0;ii<=32;ii++)
		cout << sum[ii];
}

void printfSum()
{
	cout << "\nFSUM = ";
	for(int ii=0;ii<=32;ii++)
		cout << fsum[ii];
}

void getTrueSum1()
{
	truesum1=0;
	for(int ii=1;ii<=n;ii++)
	{
		if(checkArray[ii] == 1)
			truesum1=truesum1+numarr[ii];
	}
}

void getTrueSum2()
{
	truesum2=0;
	for(int ii=1;ii<=n;ii++)
	{
		if(checkArray[ii] == 0)
			truesum2=truesum2+numarr[ii];
	}
}

bool checkEquality()
{
	for(int ii =1;ii<=32;ii++)
		if(sum1[ii] != sum2[ii])
			return false;
	return true;
}