#include<iostream>
#include<vector>
#include<fstream>
#define sz 1000
using namespace std;

struct directory
{
       vector <string> str;
       int used;
       struct directory *v[sz];
       
       
};

int construct(struct directory **temporary,vector <string> &subdir)
{
     directory* backup = *temporary;
     directory *temp = *temporary;
     int mkdir=0;
     int flag=0;
     for(int i=0;i<subdir.size();i++)
     {
             
                        int f =find(temp->str.begin(),temp->str.end(),subdir[i])-temp->str.begin();
                        if(f==temp->str.size())
                        {
                                               cout<<"create dir for "<<subdir[i]<<endl;
                           temp->used++;
                           temp->str.push_back(subdir[i]);
                           temp->v[temp->used] = new (directory);
                           temp->v[temp->used]->used=-1;                      
                           if(i==0)
                                   temporary = &temp;
                           temp = temp->v[temp->used];
                          
                           mkdir++;
                           
                        }
                        else
                        {
                            temp = temp->v[f];    
                            
                            
                        }
                 
             
             
     }     
     
     temp=backup;
     return mkdir;
     
}
int main()
{
    
    fstream input;
    string s;
    cin>>s;
    input.open(s.c_str(),ios::in);
    int T;
    
    input>>T;
    
    
    fstream output;
    output.open("output.txt",ios::out);
    
   
   for(int caseno=0;caseno<T;caseno++)
   {
           
           struct directory  *dir;
           dir = new directory;
           dir->used=-1;
           for(int i=0;i<sz;i++)
                   dir->v[i]=NULL;
                   
           int n,m;
           input>>n;
           input>>m;
           cout<<n<<" "<<m<<endl;
           for(int i=0;i<n;i++)
           {
                   string s;
                   vector <string> smalldir;
                   string temp="";
                   input>>s;
                //   cout<<s<<endl;
                   for(int index =1;index<s.size();index++)
                   {
                           if(s[index]!='/')
                           {
                                            temp+=s[index];
                           }
                           else if(s[index]=='/')
                           {
                               smalldir.push_back(temp);
                               temp="";
                                   
                               
                           }
                           
                   }  
                   smalldir.push_back(temp);
                 //  cout<<"subdirectories are "<<endl;      
                   construct(&dir,smalldir);
                   
                 
           }  
           
           int answer=0;       
           for(int i=0;i<m;i++)
           {
                  string s;
                   vector <string> smalldir;
                   string temp="";
                   input>>s;
                //   cout<<s<<endl;
                   for(int index =1;index<s.size();index++)
                   {
                           if(s[index]!='/')
                           {
                                            temp+=s[index];
                           }
                           else if(s[index]=='/')
                           {
                               smalldir.push_back(temp);
                               temp="";
                                   
                               
                           }
                           
                   }  
                   smalldir.push_back(temp);
                  // cout<<"subdirectories are "<<endl;      
                   answer+=construct(&dir,smalldir);
                   cout<<answer<<" ";
           }
           
           
           output<<"Case #"<<caseno+1<<": "<<answer<<endl;
           
   }
   
   
   
   
   
   
   
    input.close();
    output.close();
    system("pause");
    return 0;
    
        
    
    
    
}



