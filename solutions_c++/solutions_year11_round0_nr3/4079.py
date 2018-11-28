#include<iostream>
#include<string>
#include<cstring>
#include<fstream>
#include<math.h>

using namespace std;

string itob(int nn);
int btoi(string ss);
int patrickAdd(int, int);


int main()
{
int caseNum=1;
int num[100] = {0};
int t, n, j;

string ss="";
string str;
string nstr;
int nn;
int seanPile[100]={0};
int patrickPile[100]={0};
int seanSum = 0;
int patrickSum = 0;
int totalsum = 0;
int sp,pp,y,min;

ifstream fi;
fi.open("C-small-attempt1.in");
ofstream fo;
fo.open("output.txt");

if(fi.good())
	{
	getline(fi, str);
	t = atoi(&str[0]);
	
	for(int i1=0; i1<100; i1++) num[i1]=0;
	j=0;
	
	for(int i=0; i<t; i++)
		{
		for(int i1=0; i1<100; i1++) num[i1]=0;
		j=0;
		getline(fi, str);
		n = atoi(&str[0]);
		
		getline(fi, str);
		
		for(int i1=0; i1<n; i1++)
			{
			
			nstr  ="";
			while(str[j]==' ')j++;
			while(str[j]!=' ')
				{nstr = nstr + str[j];
				//nstr.append(1,str[j]);
				j++;
				}
			nn = atoi(&nstr[0]);
			num[i1]= nn;
			while(str[j]==' ')j++;
			
			}
		//cout<<" t="<<t<<endl;
		//cout<<" n="<<n<<endl;
		
		totalsum = 0;
		//for(int i1=0; i1<100; i1++)
			//{cout<<" "<<num[i1];
			//}
			
		min = num[0];
		for(int i2=0; i2<n; i2++)
			{totalsum = totalsum + num[i2];
			if(num[i2]<min)min = num[i2];
			}
		
		seanSum = patrickSum =0;
		
		for(int i1=0; i1<n; i1++)
				{//cout<<"\nmps="<<patrickSum<<"  ppile[i1]="<<patrickPile[i1]<<endl;
				//if(patrickPile[i1]==0)break;
				patrickSum = patrickAdd(patrickSum,num[i1]);
				//cout<<"\nmidpatrsum="<<patrickSum<<endl;
				}
		//cout<<"\npatSum="<<patrickSum<<endl;		
				
		if(patrickSum!=0)y=-1;
		else y = totalsum - min;
		
		
		//Select piles & check values
		/*
		for(int i1=0; i1<100; i1++)
			{seanPile[i1]=0;
			patrickPile[i1]=0;}
		
		y=-1;
		
		for(int i1=0; i1<n; i1++)ss.append("0");
		
		for(int j1=0; j1<pow(2,n)-2; j1++)
			{
			
			if(ss[n-1]=='0')ss[n-1]='1';
			else
				{cout<<"HI";
				ss[n-1]='0';
				for(int i1=n-2; i1>=0; i1++)
					{if(ss[i1]=='1' )ss[i1]='0';
					else {ss[i1]='1';break;}
					}
				
				}
			cout<<"\nss="<<ss<<endl;
			sp = pp = 0;
			
			for(int i1=0; i1<n; i1++)
				{
				if(ss[i1]==0)
					{seanPile[sp]=num[i1];sp++;}
				else
					{patrickPile[pp]=num[i1];pp++;}
				
				}
			
			seanSum = patrickSum = 0;
			
			for(int i1=0; i1<100; i1++)
				{
				if(seanPile[i1]==0)break;
				seanSum = seanSum + seanPile[i1];
				}
			//cout<<"Seansum="<<seanSum<<endl;
			for(int i1=0; i1<100; i1++)
				{//cout<<"\nmps="<<patrickSum<<"  ppile[i1]="<<patrickPile[i1]<<endl;
				if(patrickPile[i1]==0)break;
				patrickSum = patrickAdd(patrickSum,patrickPile[i1]);
				//cout<<"\nmidpatrsum="<<patrickSum<<endl;
				}
			cout<<"\ntotalsum="<<totalsum<<endl;
			//cout<<"\nPatricksum="<<patrickSum<<endl;
			if(seanSum==patrickSum && seanSum!=0 && y<(totalsum - seanSum))
				{y = totalsum - seanSum;
				continue;}
			
			
			
			
			}
		*/
		
		
		
		
		fo<<"Case #"<<caseNum<<": ";
		if(y==-1)
		fo<<"NO"<<endl;
		else fo<<y<<endl;
		caseNum++;
		}
		
		
		
		
		
		
	
	
	
	
	}
fi.close();
fo.close();



return 0;


}





string itob(int nn)
{
int n=nn;

int n1 = n;
int rem;
string str = "";

if(nn==1)return "1";
if(nn==0)return "0";

while(n1!= 1)
{
rem = n1%2;
n1 = n1/2;
//cout<<rem;
if(rem==1)str = "1"+str;
else str = "0"+str;
}
str = "1"+str;

return str;

}

int btoi(string ss)
{
string str = ss;
int l = str.length();
int n = 0;
int x = 1;

for(int i=l-1; i>=0; i--)
	{
	if(str[i]=='1') n = n + x;
	x = x*2;
	}

return n;


}


int patrickAdd(int a, int b)
{

string astr, bstr, cstr, c1str;
int al, bl, cl, c;

c=0;
cstr = "";
astr = itob(a);
bstr = itob(b);
al = astr.length();
bl = bstr.length();

//cout<<"\nastr="<<astr<<"  bstr="<<bstr<<endl;

if(al<bl)
	{
	int xl;
	xl = al;
	al = bl;
	bl = xl;	
	string x;
	x = astr;
	astr = bstr;
	bstr = x;
	}


	//Now al>=bl
	
	cl = al;
	
	string b1="";
	for(int i=0; i<al-bl;i++)
		{
		b1.append("0");
		}
	b1.append(bstr);
	//cout<<"\nb1= "<<b1;
	/*
	string c1str="";
	for(int i=bl-1; i>=0; i--)
		{
		if((astr[cl-1-i]=='1'&&bstr[cl-1-i]=='0')||(astr[cl-1-i]=='0'&&bstr[cl-1-i]=='1'))cstr.append(str1);
		else if((astr[cl-1-i]=='0'&&bstr[cl-1-i]=='0')||(astr[cl-1-i]=='1'&&bstr[cl-1-i]=='1'))cstr.append(str0);
		
		}
	
	for(int i=al-1; i>=bl; i--)
		{
		c1str.append(1,astr[cl-1-i]);
		}
		c1str.append(cstr);
	*/
	
	for(int i=0; i<cl; i++)
		{
		if(astr[i]==b1[i])c1str.append("0");
		else c1str.append("1");
		
		}
	
	
	// string dstr="";
	// for(int i=0; i<cl; i++)
		// {
		// dstr.append(1,c1str[cl-i-1]);
		// }
	// cout<<"\nastr="<<astr<<endl;
	// cout<<"\nbstr="<<bstr<<endl;
	// cout<<"\nc1str="<<c1str<<endl;
	// cout<<"\ndstr="<<dstr<<endl;
	 c = btoi(c1str);

return c;









}



