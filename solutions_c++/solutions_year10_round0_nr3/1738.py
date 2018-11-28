#include<iostream>
#include<fstream>
#include<vector>
using namespace std;
struct node
{
       int nextindex;
       long long int answer;
              
       
};
int main()
{
    
    string s;
    cin>>s;
    
    fstream input;
    input.open(s.c_str(),ios::in);
    int cases;
    input>>cases;
    vector <int> tempans;
    fstream output;
    output.open("output.txt",ios::out);
    
    
    for(int i=0;i<cases;i++)
    {
            long long int ans=0;
            int r,k,n;
            input>>r>>k>>n;
            vector <int> g(n);
            for(int temp=0;temp<n;temp++)
                    input>>g[temp];
            vector <node> memoize(n);
            for(int loop=0;loop<n;loop++)
            {
                    int index=loop;
                    long long int answer=0;
                    int inclindex=0;
                    while(answer<k&&inclindex<n)
                    {
                                   answer+=g[index];
                                   index=(index+1)%n;
                                   inclindex++;
                                                  
                    }
                    if(answer>k)
                    {
                                index--;
                                if(index==-1)
                                             index=n-1;
                                 answer-=g[index];        
                    }
                    memoize[loop].nextindex=index;
                    memoize[loop].answer=answer;
                    
            }
            
            int index=0;
                    
            for(int round=0;round<r;round++)
            {
                    ans+=memoize[index].answer;
                    index = memoize[index].nextindex;
                            
                    
            }
                           
            output<<"Case #"<<i+1<<": "<<ans<<endl;
            
    }    
    
    output.close();
    input.close();
    system("pause");
    return 0;
    
    
    
    
    
}
