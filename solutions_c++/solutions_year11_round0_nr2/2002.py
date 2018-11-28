#include<iostream>
using namespace std;
int main(){
    bool exc[26][26]={0};
    char com[26][26]={0},a,b,c,str[105];
    int test=0,T,C,N,D,s1,i,j,k,present[26]={0};
    cin>>T;
    while(T--){
        for(i=0;i<26;i++){
            present[i]=0;
            for(j=0;j<26;j++)
                exc[i][j]=com[i][j]=0;
        }
        cin>>C;
        for(i=0;i<C;i++){
            cin>>a>>b>>c;
            com[a-'A'][b-'A']=com[b-'A'][a-'A']=c;
        }
        cin>>D;
        for(i=0;i<D;i++){
            cin>>a>>b;
            exc[a-'A'][b-'A']=exc[b-'A'][a-'A']=1;
        }
        cin>>N;
        s1=0;
        for(i=0;i<N;i++){
            cin>>a;
            str[s1]=a;
            if((s1>0) && (com[a-'A'][str[s1-1]-'A']!=0))
                {
                    present[str[s1-1]-'A']--;
                    str[s1-1]=com[a-'A'][str[s1-1]-'A'];
                }
            else{
                for(j=0;j<26;j++)
                    if((exc[a-'A'][j]==1) &&(present[j]>0))
                    {
                        s1=0;
                        for(k=0;k<26;k++)present[k]=0;
                        break;
                    }
                 if(j==26){s1++;present[a-'A']++;}
            }
        }
        str[s1]='\0';
        test++;
        cout<<"Case #"<<test<<": [";
        for(i=0;i<s1-1;i++)cout<<str[i]<<", ";
        if(s1>0)cout<<str[s1-1]<<"]"<<endl;
        else cout<<"]"<<endl;
    }
    return 0;
}
           
