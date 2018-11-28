#include<cstdio>
#include<algorithm>
#include<vector>
#include<list>
#include<queue>
#include<stack>
#include<string>
#include<iostream>
using namespace std;

struct node{
     node(string f,node *p=NULL, node* l=NULL, node* r=NULL): f(f), l(l), r(r), p(p), lab(false) {};
     string f;
     double prob;
     node *l,*r;
     node *p;
     bool lab;
     
};
vector<string> F;
int k;

double count(node *cur) {
    // printf("in %lf\n",cur->prob);
     if (!cur->lab) return cur->prob;
     bool yes=false;
     for (int i=0; i<k; i++) {
	// cout << F[i] << " vs " << cur->f <<endl;
	  if (F[i]==cur->f)   yes=true;
     }
     if (yes) return cur->prob*count(cur->l);
     else return cur->prob*count(cur->r);
    
}
int solve(int no) {
     int l;
     scanf("%d",&l);
     node root("");
     string s;
     printf("Case #%d:\n",no+1);
     char a=getchar();
     node *cur=&root;
     bool beg=true;
     while (a!='(' && a!=')') a=getchar();
     while (true ) {
	  if (a=='(') {
	       if (!beg) {
		    if (cur->l==NULL) {
			 cur->l=new node("",cur);
			 cur=cur->l;
		//	 printf("L\n");
		    }
		    else {
			 cur->r=new node("",cur);
			 cur=cur->r;
		//	 printf("R\n");
		    }
		    
	       }
	       beg=false;
	       scanf("%lf",&cur->prob);
	     //  printf("p=%lf\n",cur->prob);
	       a=getchar();
	       while(a!=')' && (a<'a' || a>'z')) a=getchar();
	       string s="";
	       while(a>='a' && a<='z') {
		    s=s+a;
		    cur->lab=true;
		    a=getchar();
	       }
	    //   cout << s << endl;
	       if (cur->lab) cur->f=s;
	       while(a!=')' && a!='(') a=getchar();
	  }
	  else if (cur!=&root) {
	       cur=cur->p;
	       a=getchar();
	       while(a!=')' && a!='(') a=getchar();
	  }
	  else break;
     }
     int an;
     scanf("%d",&an);
     
     for (int i=0; i<an; i++) {
	  while(a<'a' || a>'z') a=getchar();
	  while(a!=' ') {
	       a=getchar();
	//       printf("%c\n",a);
	  }
	  scanf("%d",&k);
	  F.resize(k);
	  for (int j=0; j<k; j++) {
	       while (a<'a' || a>'z') {
		    a=getchar();
	       }
	       F[j]="";
	       while(a>='a' && a<='z') {
		    F[j]=F[j]+a;
		    a=getchar();
	       }
	//       cout << k << " " << j << F[j] << endl;
	  }
	  printf("%.9lf\n",count(&root));
     }
     return 0;
}
     

int main() {
     int n;
     scanf("%d",&n);
     for (int i=0; i<n; i++) solve(i);
     return 0;
}