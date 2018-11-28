#include<iostream>
using namespace std;
char com[40][3],opp[40][2];
int searchcom(char a,char b,int c)
{
    int i;
    if(a>b)
       return searchcom(b,a,c);
    else
    {
        for(i=0;i<c;i++)
        {
                        if(com[i][0]==a && com[i][1]==b)
                        return i;
        }
    }
    return -1;
}

int searchopp(char a,char b,int d) 
{
    int i;
    if(a>b)
       return searchopp(b,a,d);
    else
    {
     for(i=0;i<d;i++)
        {
                        if(opp[i][0]==a && opp[i][1]==b)
                        return i;
        }
}
    return -1;
}
            
           
int main()
{
    int t,i,j,k,k1,d,c,n,m;
    char ans[102],temp;
    bool br;
   
    cin>>t;
    for(i=0;i<t;i++)
    {
                    cin>>c;
                    for(j=0;j<c;j++)
                    {
                                    cin>>com[j][0]>>com[j][1]>>com[j][2];
                                    if(com[j][0]>com[j][1]){temp=com[j][0];com[j][0]=com[j][1];com[j][1]=temp;}
                    }
                    cin>>d;
                    for(j=0;j<d;j++)
                    {
                                    cin>>opp[j][0]>>opp[j][1];
                                    if(opp[j][0]>opp[j][1]){temp=opp[j][0];opp[j][0]=opp[j][1];opp[j][1]=temp;}
                    }
                    
                    cin>>n;
                    cin>>ans[0];
                    k=1;
                    
                    for(j=1;j<n;j++)
                    {
                                   
                                 cin>>ans[k];
                                 k++;
                                 if(k!=1)
                                 {
                                                  
                                                  k1=searchcom(ans[k-1],ans[k-2],c);
                                                  if(k1!=-1)
                                                  {ans[k-2]=com[k1][2];
                                                  k=k-1;}
                                 }
                                 if(k1==-1){
                                 br=false;
                                 for(m=0;m<(k-1);m++)
                                 {
                                                     if(searchopp(ans[m],ans[k-1],d)!=-1)
                                                     {br=true;break;}
                                 }
                                 if(br==true)
                                 k=0;
                                 }
                                 
                    }
                    cout<<"Case #"<<(i+1)<<": [";
                    if(k>1){
                    for(m=0;m<(k-1);m++)
                    cout<<ans[m]<<", ";
                    cout<<ans[k-1]<<"]"<<endl;}
                    else if(k==0)cout<<"]"<<endl;
                    else
                    {cout<<ans[0]<<"]"<<endl;}
                        
    }
    return 0;
}  
