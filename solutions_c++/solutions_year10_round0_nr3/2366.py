#include<iostream>
#include<queue>
using namespace std;

int x[1003];
struct AAA
{
int n;
int v;
};
int main()
{
    int t;
    cin>>t;
for(int i=1;i<=t;i++)
{
        
        int r,k,n;
        cin>>r>>k>>n;
queue<AAA>q;
        AAA f;
        for(int i=1;i<=n;i++)
        {
        cin>>x[i];
        f.n=i;
        f.v=x[i];
        q.push(f);
        }
        int a=0;
        int b=0;
for(int i=1;i<=r;i++)
{
        
        if(i!=1&&q.front().n==1)
        {
                  a=a*(r/(i-1));
                  r=r-r/(i-1)*(i-1);    
                  i=1;
                  //system("pause");
                  if(r==0)break;  
        }
int mn=q.front().n;
int p=0;
bool ff=0;

while((q.front().n!=mn)||ff==0)
{

       if(p+q.front().v>k)break; 
       
       f=q.front();
       q.pop();
       q.push(f);
       p=p+f.v;
       ff=1;
      // cout<<mn<<" "<<q.front().n<<" "<<f.n<<" "<<f.v<<endl;
      // system("pause");
}
a=a+p;

}        
cout<<"Case #"<<i<<": "<<a<<endl;



 //dhbfbfbfnenrhegr   
}
    
    return 0;
}
