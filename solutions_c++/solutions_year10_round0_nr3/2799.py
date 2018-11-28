
# include <iostream>
# include <queue>

using namespace std;

queue <int> ar;
int k,i,j,n,r,s;

int checkav()
{
    int euro1=0,i,j,seat=1,tmp,k1,sz;
    sz = ar.size();
    k1 = k;
    while((ar.front() <= k1) && (sz != 0))     
         {
                k1 -= ar.front();
                euro1 += ar.front();
                --sz;
                tmp = ar.front();
                ar.pop();
                ar.push(tmp); 
         }    
    return euro1;
}

int main()
{
    int t,l;
    cin>>t;
    for(l=1;l<=t;l++)
    {
         //vector <int> ar(1000000000,0);
         int euro=0;
         cin>>r>>k>>n;
         for(i=0;i<n;i++)
         {
                cin>>s;
                ar.push(s);                
         }
         //cout<<ar.size()<<endl;
         for(i=0;i<r;i++)
         {
                euro += checkav();     
                //cout<<euro<<endl;        
         }
         cout<<"Case #"<<l<<": "<<euro<<endl;
         while (!ar.empty())
         {
               ar.pop();
         }
    }
    //system("pause");    
}
