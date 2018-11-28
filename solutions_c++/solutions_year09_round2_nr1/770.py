#include<iostream>
#include<iomanip>
#include<sstream>
#include<fstream>
using namespace std;
ifstream fin("A-large_1.in");
ofstream fout("TREE.OUT");
#define MAX 10001
#define MAXCHUOI 2000

struct node{
    double w;
    string s;
    node* left;
    node* right;
};

node* root;
char tam[MAXCHUOI];

int Find(string s){
   for(int i=s.length()-1;;i--)
       if(s[i]==')'){
          return i;
          break;
       }
}

void Nhap(int begin, int end,string s,node*& root){
   int i;
   int ntam=0;
   for(i=begin+1;i<end;i++){
       if(s[i]=='(')
          break;
       else
          tam[ntam++]=s[i];
   }
   tam[ntam]='\0';
   stringstream ss;
   ss<<tam;
   node* temp=new node;
   ss>>temp->w;
   ss>>temp->s;
   root=temp;
   if(!temp->s.length())
       return;
   //tim con trai va con phai cua chuoi s
   //tim con trai
   int dautrai;
   int dauphai;
   int songoac=0;
   for(i=begin+1;i<end;i++)
       if(s[i]=='('){
           dautrai=i;
           break;
       }
   for(i=dautrai;i<end;i++)
       if(s[i]=='(')
           ++songoac;
       else if(s[i]==')'){
           --songoac;
           if(!songoac){
              dauphai=i;
              break;
           }
       }
    Nhap(dautrai,dauphai,s,root->left);
    //tim con phai
    for(i=dauphai+1;i<end;i++)
       if(s[i]=='('){
           dautrai=i;
           break;
       }
    for(i=dautrai;i<end;i++)
       if(s[i]=='(')
           ++songoac;
       else if(s[i]==')'){
           --songoac;
           if(!songoac){
              dauphai=i;
              break;
           }
       }
    Nhap(dautrai,dauphai,s,root->right);
}

bool Sastified(string s,string P[],int nP){
   for(int i=1;i<=nP;i++)
       if(s==P[i])
           return true;
   return false;
}

//duyet NLR
double CheckP(node* root,string P[],int nP){
   //cout<<A[pos].w<<" "<<A[pos].s<<endl;
   if(!root->s.length())
       return root->w;
   if(Sastified(root->s,P,nP))
       return root->w*CheckP(root->left,P,nP);
   else
       return root->w*CheckP(root->right,P,nP);
}

void proccess(int t){
   int n=1,q,i,j;//n dong, q truy van
   int dau,cuoi;//nP so tinh chat cua DV
   fin>>n;
   fin.ignore();
   string str,s,name;
   node temp;
   
   for(i=1;i<=n;i++){
       getline(fin,str);
       s+=str;
   }
   root=new node;
   Nhap(0,Find(s),s,root);
   fin>>q;
   fout<<"Case #"<<t<<":\n";
   while(q--){
       double kq;
       string P[MAX];
       int nP;
       fin>>name>>nP;
       for(i=1;i<=nP;i++)
           fin>>P[i];
       kq=CheckP(root,P,nP);//kiem tra cac tinh chat cua DV
       fout<<setiosflags(ios::fixed|ios::showpoint)<<setprecision(7)<<kq<<endl;
   }
}

int main(){
   int T;
   fin>>T;
   for(int t=1;t<=T;t++)
      proccess(t);
   //system("pause");
   return 0;
}
