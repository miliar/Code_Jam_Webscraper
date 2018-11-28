#include<iostream>
using namespace std;
struct node{
    node * link[26];
    int pos;
};
void ins(node * n,int pos, char s[17],int len){
    //cout<<s[pos];
    if(pos==len)return;
    if(n->link[s[pos]-'a']!=NULL){
        
        ins(n->link[s[pos]-'a'],pos+1,s,len);
    }
    else{
        //cout<<s[pos];
        node *tmp=new node;
        (tmp->pos)=(n->pos)+1;
        for(int i=0;i<26;i++)tmp->link[i]=NULL;
        n->link[s[pos]-'a']=tmp;
        ins(tmp,pos+1,s,len);
        }
    }
int check(node* n,int pos,int l, char s[425],int p,int len){
    int no=0;
    if(p==len||pos==l)return 1;
    if(s[p]!='('){
        if(n->link[s[p]-'a']!=NULL)
        no=check(n->link[s[p]-'a'],pos+1,l,s,p+1,len);
    }
    else if(s[p]=='(')
    {
        p++;
        int pos1=p;
        while(s[pos1++]!=')');
        while(p<pos1-1)
        {
            if(n->link[s[p]-'a']!=NULL)
            no+=check(n->link[s[p]-'a'],pos+1,l,s,pos1,len);
            p++;
        }
    }
    return no;
    }

int main()
{
    int no,i,j,l,d,n,num=0;
    char s[17];
    char test[425];
    cin>>l>>d>>n;
    node * start=new node;
    start->pos=0;
    for(i=0;i<26;i++)start->link[i]=NULL;
    for(i=0;i<d;i++){
        cin>>s;
        ins(start,0,s,l);
    }
    for(i=0;i<n;i++){
        cin>>test;
        j=0;
        while(test[j++]);
        
        no=check(start,0,l,test,0,j);
        cout<<"Case #"<<i+1<<": "<<no<<endl;
    }
    return 0;
}
