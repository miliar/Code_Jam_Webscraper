#include<iostream>
#include<iomanip>
#include<sstream>
#include<fstream>
using namespace std;
ifstream fin("A-small-attempt0.in");
ofstream fout("TREE.OUT");
#define MAX 201
struct node{
    double w;
    string s;
};

node A[MAX];


int Find(string s){
   for(int i=s.length()-1;;i--)
       if(s[i]==')'){
          return i;
          break;
       }
}

void Nhap(int begin, int end,string s,int pos){
   int i;
   char tam[MAX];
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
   node temp;
   ss>>temp.w;
   ss>>temp.s;
   A[pos]=temp;
   if(!temp.s.length())
       return;
   //cout<<A[pos].w<<" "<<A[pos].s<<endl;
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
    Nhap(dautrai,dauphai,s,pos*2+1);
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
    Nhap(dautrai,dauphai,s,pos*2+2);
}

bool Sastified(string s,string P[],int nP){
   for(int i=1;i<=nP;i++)
       if(s==P[i])
           return true;
   return false;
}

//duyet NLR
double CheckP(int pos,string P[],int nP){
   //cout<<A[pos].w<<" "<<A[pos].s<<endl;
   if(!A[pos].s.length())
       return A[pos].w;
   if(Sastified(A[pos].s,P,nP))
       return A[pos].w*CheckP(pos*2+1,P,nP);
   else
       return A[pos].w*CheckP(pos*2+2,P,nP);
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
   Nhap(0,Find(s),s,1);
   fin>>q;
   fout<<"Case #"<<t<<":\n";
   while(q--){
       double kq;
       string P[MAX];
       int nP;
       fin>>name>>nP;
       for(i=1;i<=nP;i++)
           fin>>P[i];
       kq=CheckP(1,P,nP);//kiem tra cac tinh chat cua DV
       fout<<setiosflags(ios::fixed|ios::showpoint)<<setprecision(7)<<kq<<endl;
   }
}
int main(){
   int T;
   fin>>T;
   for(int t=1;t<=T;t++)
      proccess(t);
//   system("pause");
   return 0;
}
