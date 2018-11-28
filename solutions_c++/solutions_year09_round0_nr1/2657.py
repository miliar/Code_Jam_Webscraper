#include<iostream>
#include<fstream>
#include<string>
using namespace std;

char dict[5000][16];
char a[20][30];
int l,d,n;
int main()
{
ifstream fin;
ofstream fout;
freopen("C:\\Temp\\inpu.txt","rt",stdin);
freopen("C:\\Temp\\output.txt","wt",stdout);
int check();
cin>>l;
cin>>d;
scanf("%d\n",&n);

int index=0;
while(index<d)
{
scanf("%s\n",dict[index]);
index++;
}
int case_n=1;
while(case_n<=n)
{
char temp[600];
scanf("%s\n",temp);
int j=0,k=0;
for(int i=0;temp[i]!='\0';)
{
k=0;
if(temp[i]=='(')
{
i++;
while(temp[i]!=')')
{a[j][k]=temp[i];
k++;
i++;}
}//end of if
else
{
a[j][k]=temp[i];
k++;
}
i++;
a[j][k]='\0';
j++;
}
int ans=check();
cout<<"Case #"<<case_n<<": "<<ans<<endl;
case_n++;

}//end of case
fin.close();
fout.close();
return 0;
}

int check()
{
int count=0;
int flag;
for(int i=0;i<d;i++)
{ flag=1;
for(int j=0;j<l;j++)
{
if(strchr(a[j],(int)dict[i][j])==NULL)
flag=0;
}
if(flag)
count++;        
}//end of for int i 
return count;
}
