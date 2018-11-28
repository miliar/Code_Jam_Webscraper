# include <iostream>
# include <map>
# include <vector>
# include <algorithm>
# include <cstdio>


using namespace std;
vector<string> vs;
  
int allin(map<string,int> m,int fl,string pre)
{
    int f=1;
    
    //one switch has already occured
    if(fl)
    {
        for(int i=0;i<vs.size();i++)
            if(vs[i]!=pre && m[vs[i]]==0)
                f=0;
                
        return f;                
    }
        
    for(int i=0;i<vs.size();i++)
    {
        if(m[vs[i]]==0)
            f=0;
    }
return f;
}

int main()
{
    int n,cas=0;
    FILE *fin,*fout;
    fin = fopen("A-large.in","r");
    fout = fopen("A-large.txt","w");
    
    fscanf(fin,"%d",&n);
  //  cin>>n;
    
    while(n--)
    {
        int s,q,c=0;
        map<string,int> m;
        char str[105];
      
        vs.clear();        
        fscanf(fin,"%d\n",&s);
      //  cin>>s;
       
        for(int i=0;i<s;i++)
        {
             fgets(str,105,fin);
            //cin>>str;
            m[str]=0;
            vs.push_back(str);
        }
        
           
        fscanf(fin,"%d\n",&q);
       //cin>>q;
      
        int f=0;
        string pre="";
        for(int i=0;i<q;i++)
        {
            fgets(str,105,fin);
             m[str]=1;
          //cin>>str;
            if(allin(m,f,pre)){
                c++;
                f=1;
                pre=str;             
                for(int i=0;i<s;i++)
                {
                    m[vs[i]]=0;
                }
            }
           
        }
        
        fprintf(fout,"Case #%d: %d\n",++cas,c);
        //cout<<"Case #"<<++cas<<" "<<c<<'\n';
    }
  
       
    return 0;
}
            
        
        
    
