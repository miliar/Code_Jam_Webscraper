#include<iostream>
#include<string>
#include<sstream>
#include<cstdio>

using namespace std;

int check(string a,string b);


int main()
{
	freopen("A-small-attempt0.in","r",stdin); 
	freopen("result.out","w",stdout);

	int N,winX=0,winY=0,space=0,count=0;
	cin>>N;
	cin.ignore();

	while(N--){
		count++;
		winX=0;
		winY=0;
		space=0;

		string s, in[4];
		
		for(int i=0;i<4;i++){
			//cout<<"IN \n";
			getline(cin,s);
			istringstream is(s);
			is>>in[i];
			//cout<<s<<endl;
		}

		
	//check rows
	for(int i=0;i<4;i++){
		winX = winX + check(in[i],"X");
		winY = winY + check(in[i],"O");
	}

	//check columns
	string temp;
//	temp = " ";
	for(int i=0;i<4;i++){
		temp = in[0][i];
		for(int j=1;j<4;j++){

			temp += in[j][i];

		}

		
		winX = winX + check(temp,"X");
		winY = winY + check(temp,"O");
		temp = " ";
	
	}

	//check diagonals
	temp = in[0][0];
	for(int i=1;i<4;i++){
		for(int j=1;j<4;j++){
		if(i==j)
			temp +=in[i][j];


		}
	}

	winX = winX + check(temp,"X");
	winY = winY + check(temp,"O");

	temp = in[0][3];
	for(int i=1;i<4;i++)
		for(int j=0;j<4;j++)
			if(i+j==3)
				temp +=in[i][j];

	winX = winX + check(temp,"X");
	winY = winY + check(temp,"O");

	//check for space

	for(int i=0;i<4;i++)
		space = check(in[i],".");
/*
	cout<<"TEST\n";
	cout<<"winX = "<<winX<<endl;
	cout<<"winY = "<<winY<<endl;
	cout<<"space = "<<space<<endl;
*/



	if(winX==0 && winY==0 && space == 0)
		printf("Case #%d: Draw\n",count);
	else if(winX!=0)
		printf("Case #%d: X won\n",count);
	else if(winY!=0)
		printf("Case #%d: O won\n",count);
	else 
		printf("Case #%d: Game has not completed\n",count);


	getline(cin,s);
	}

	return 0;

}



int check(string a,string b)
{
	if(b=="X"){

		int count1=0,count2=0;
		for(int i=0;i<4;i++){
			if(a[i] == 'X')
				count1++;
			if(a[i] == 'T')
				count2=1;
		}

	

		if(count1==4)
			return 1;
		else if(count1==3 && count2==1)
			return 1;
		else
			return 0;
	}
	else if(b=="O"){
		int count1=0,count2=0;
		for(int i=0;i<4;i++){
			if(a[i] == 'O')
				count1++;
			if(a[i] == 'T')
				count2=1;
		}

		
		if(count1==4)
			return 1;
		else if(count1==3 && count2==1)
			return 1;
		else
			return 0;

	}
	else if(b=="."){
		int count1=0;
		for(int i=0;i<4;i++)
			if(a[i] == '.')
				count1=1;
		if(count1==1)
			return 1;
		else
			return 0;
	}

}