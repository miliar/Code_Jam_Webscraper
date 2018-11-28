
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int N,M,ans=0,pt=1;
char str[200];

struct Node{
    int left,right;
    string s; 
}nodes[100000];


void Init()
{
    for(int i=0;i<=(N+M)*100;++i) {
        nodes[i].left = nodes[i].right = 0;
        nodes[i].s = "";
    }
    ans = 0;
}

void Insert( bool ct)
{
    int index=1;
    int curpt=0;
    int len  = strlen(str);
    while(index<len){
        string s="";
        while(index<len && str[index]!='/'){
            s = s + str[index++];
        }

        //cout<<"s="<<s<<endl;
        
        index++;
        
        while( nodes[curpt].right != 0 && s != nodes[curpt].s  ){
            curpt = nodes[curpt].right;

        }
        
        if( s==nodes[curpt].s ){
            //puts("match");
            
            if( nodes[curpt].left==0 )
                nodes[curpt].left = pt++;
                
            curpt = nodes[curpt].left;
        }else{
            
            nodes[curpt].right = pt++;
            int i = nodes[curpt].right ;
            nodes[i].s = s;
            
            nodes[i].left = pt++;
            
            
            curpt = nodes[i].left;
            
            if(ct)ans++;
        }
        
        //printf("curpt=%d index=%d pt=%d ans=%d\n",curpt,index,pt,ans);
        
    }
    
    //for(int i=0;i<pt;++i)cout<<"i="<<i<<"-->"<<"("<<nodes[i].left<<","<<nodes[i].right
    //                    <<","<<nodes[i].s<<")\n";
    
}


int main()
{
    
    freopen("A-large.in","r",stdin); freopen("A-large.out","w",stdout);
    
    
    int t,cs;
    scanf("%d",&t);
    cs=0;
    while(++cs<=t){

        scanf("%d%d",&N,&M);
        
        Init();
        
        for(int i=0;i<N;++i){
            scanf("%s",str);
            Insert( false );
        }
        
        for(int i=0;i<M;++i){
            scanf("%s",str);
            Insert(true);
        }

        printf("Case #%d: %d\n",cs,ans);
    }
    
    return 0;    
}
