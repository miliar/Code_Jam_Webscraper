#include<iostream>
#include<fstream>
#include<algorithm>
#include<string>
#include<sstream>


using namespace std;
int m=2000;

int main()
{
    cout<<4<<"\n";
    
    char* in1="in.txt";
    char* ou1="ou.txt";
 	ifstream file1;//("incs.txt",ios:in);
 	
    file1.open(in1);
    ofstream file2;
    
	int T;int n;int ans;int u1;int u4;
    string sol[20000];
	file1>>T;
	int dat[100][2000];
	
	u1=0;
    while(u1<T)
	{
	file1>>n;
	for(int u3=0;u3<2000;u3++)
	{			if(u3<n)file1>>dat[u1][u3];
				else dat[u1][u3]=-1;
            
                      
	}

	u1++; 
 
    }
    file1.close();
    
    for(int u2=0;u2<T;u2++)
	{
		int b=1;
		sort(dat[u2],dat[u2]+b);
        int xor2=dat[u2][0];
		cout<<"s ";
		while(dat[u2][b]>0)
		{xor2=xor2 ^ dat[u2][b];
		 b++;	                
		}
		cout<<"\n";
		cout<<"y "<<xor2<<"\n";
		if(xor2!=0){sol[u2]="NO";}
		else
		{	  
          sort(dat[u2],dat[u2]+b);
		  ans=0;
          for(int u3=1;u3<b;u3++)
          {ans=ans+dat[u2][u3];
          }
          stringstream ch;
          ch<<ans;
          ch>>sol[u2];        
         }  
	}   
	
    file2.open(ou1);
    u4=0;
    while(u4<T)
	{
			cout<<u4<<"\n";
            file2<<"Case #";
            file2<<u4+1;
            file2<<": ";
            file2<<sol[u4];
            file2<<"\n";u4++;
    }
	file2.close();//f

cin.get();
    return 0;	  
}
