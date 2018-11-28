#include <iostream>

using namespace std;

char combination[72][3];
char destruction[56][2];

char searchc(char a, char b,int n)
{
	int i;
	//cout<<"--------"<<a<<b<<n<<endl;
	for(i=0;i<n;i++)
	{//cout<<"*****"<<combination[0][0]<<combination[0][1]<<endl;
		if(combination[i][0]==a && combination[i][1]==b)
			return combination[i][2];
	}
	return '.';
}

bool searchd(char a, char b, int n)
{
	//cout<<"a:"<<a<<"b:"<<b<<"n:"<<n<<endl;
	int i;
	for(i=0;i<n;i++)
	{	
		if(destruction[i][0]==a && destruction[i][1]==b)
			return true;
	}
	return false;
}

int main()
{
	int t,c,d,n;
	char str[100];
	int ct=0;
	int i,j,k;
	int testCase=1;

	cin>>t;
	while(t--)
	{
		ct=c=d=0;
		cin>>c;
		//combination elements
		for(i=0;i<c;i++)
		{
			cin>>combination[i][0]>>combination[i][1]>>combination[i][2];
			combination[i+1][1]=combination[i][0];
			combination[i+1][0]=combination[i][1];
			combination[i+1][2]=combination[i][2];
			i+=1;
		}
		//cout<<"*****"<<combination[0][0]<<combination[0][1]<<endl;
/*		for(i=0;i<ct;i++)
			cout<<combination[i][0]<<combination[i][1]<<combination[i][2]<<endl;*/
		ct=0;
		//destruction elements
		cin>>d;
		for(i=0;i<d;i++)
		{
			cin>>destruction[ct][0]>>destruction[ct][1];
			destruction[ct+1][1]=destruction[ct][0];
			destruction[ct+1][0]=destruction[ct][1];
			i+=1;
		}
		/*		for(i=0;i<ct;i++)
			cout<<destruction[i][0]<<destruction[i][1]<<endl;*/
		//reading string;
		ct=0;
		j=1;
		cin>>n;
		cin>>str[0];
		for(i=1;i<n;i++)
		{
			cin>>str[j];
		if(c!=0)
		{
			char t1=searchc(str[j],str[j-1],c*2);
		//	cout<<"t1="<<t1<<endl;
			if(t1 != '.')
			{
				str[j-1]=t1;
				//cout<<"j:"<<j<<"  "<<"str[j-1]="<<str[j-1]<<"  "<<"printing str: "<<endl;
				/*for(ct=0;ct<j;ct++)
					cout<<str[ct];*/
			//	cout<<endl;
				continue;
			}
			else j++;
		}	
		else j++;

		if(d!=0)
		{	
			for(k=0;k<j;k++)
			{
				bool t2 = searchd(str[k],str[j-1],d*2);
			//	cout<<"t2:"<<t2<<endl;
				if(t2==true)
				{
					j=0;
					break;
				}
			}
		}
		}
//		cout<<"J="<<j<<endl;
		
		cout<<"Case #"<<testCase<<": [";
		if(j==0) cout<<"]"<<endl;
		else{
		for(i=0;i<j-1;i++)
		cout<<str[i]<<", ";
		cout<<str[i]<<"]"<<endl;}
		testCase+=1;
	}

return 0;
}
