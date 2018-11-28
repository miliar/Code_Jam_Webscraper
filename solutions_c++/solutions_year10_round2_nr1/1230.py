#include<cstdio>
#include<iostream>
#include<fstream>
#include<map>
#include<string>

using namespace std;
    
struct node
{
    map<string,node*> children;
};

int main()
{
    int i,j,k;
    ifstream fin("A-large.in");
    FILE* fp=fopen("A_large.txt","w+");
    
    int T,N,M,ans,leng,start,node_index;
    string input,temp_char;
    fin>>T;
    node no[10000];
    node *current;
    map<string,node*>::iterator iter;
    for(i=0;i<T;++i)
    {
        ans=0;
        node_index=1;
        fin>>N>>M;
        
        for(j=0;j<N;++j)
        {         
            fin>>input;            
            leng=input.length();
            current=&no[0];

            start=1;
            for(k=1;k<leng;++k)
            {
                if(input[k]=='/')
                {
                    temp_char=input.substr(start,k-start);
                    iter=current->children.find(temp_char);
                    if(iter==current->children.end())
                    {
                        current->children.insert(make_pair(temp_char,&no[node_index]));
                        current=&no[node_index];
                        
                        
                        //cout<<"create "<<temp_char<<" : "<<&no[node_index]<<endl;
                        
                        ++node_index;
                    }
                    else
                    {
                        current=iter->second;
                        
                        //cout<<"found "<<temp_char<<" : "<<current<<endl;
                    }
                    start=k+1;
                }
            }
            temp_char=input.substr(start,k-start);
            iter=current->children.find(temp_char);

            if(iter==current->children.end())
            {
                current->children.insert(make_pair(temp_char,&no[node_index]));
                current=&no[node_index];
                //cout<<"create "<<temp_char<<" : "<<&no[node_index]<<endl;
                
                ++node_index;
            }
            else
            {
                current=iter->second;
                
                //cout<<"found "<<temp_char<<" : "<<current<<endl;
            }
        }
        
        //cout<<"test phase"<<endl;
        
        for(j=0;j<M;++j)
        {         
            fin>>input;            
            leng=input.length();
            current=&no[0];

            start=1;
            for(k=1;k<leng;++k)
            {
                if(input[k]=='/')
                {
                    temp_char=input.substr(start,k-start);
                    iter=current->children.find(temp_char);
                    if(iter==current->children.end())
                    {
                        current->children.insert(make_pair(temp_char,&no[node_index]));
                        current=&no[node_index];
                        
                        
                        //cout<<"create "<<temp_char<<" : "<<&no[node_index]<<endl;
                        
                        ++ans;
                        ++node_index;
                    }
                    else
                    {
                        current=iter->second;
                        
                        //cout<<"found "<<temp_char<<" : "<<current<<endl;
                    }
                    start=k+1;
                }
            }
            temp_char=input.substr(start,k-start);
            iter=current->children.find(temp_char);

            if(iter==current->children.end())
            {
                current->children.insert(make_pair(temp_char,&no[node_index]));
                current=&no[node_index];
                
                //cout<<"create "<<temp_char<<" : "<<&no[node_index]<<endl;
                
                ++ans;
                ++node_index;
            }
            else
            {
                current=iter->second;
                
                //cout<<"found "<<temp_char<<" : "<<current<<endl;
            }
        }
        
        fprintf(fp,"Case #%d: %d\n",i+1,ans);
        for(j=0;j<node_index;++j)
        {
            no[j].children.clear();
        }
    }
    fclose(fp);
    //system("pause");
    return 0;
}
