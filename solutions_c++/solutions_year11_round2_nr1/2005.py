#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<queue>
#include<vector>
#include<map>
#include<stack>
#include<algorithm>

using namespace std;

typedef vector<int> vi;
typedef vector<float> vf;

#define For(i,a,b) for (int i(a),_b(b);i<b;i++)
#define Rep(i,a) for (int i(0),_a(a);i<a;i++)
#define Repd(i,a) for (int i(a),_a(a);i>0;i--)

int main(void){
 freopen("A-large.in","rt",stdin);
  freopen("output.txt","wt",stdout);
  int cases;
  scanf("%d\n",&cases);

  Rep(i,cases){
    int no;
    scanf("%d\n",&no);
    char ar[no][no];
    double wp[no];
    double owp[no];
    double oowp[no];
    Rep(j,no){
      double l=0,m=0;
	scanf("%s",&ar[j]);
      Rep(k,no){

	if(ar[j][k]=='1'){
	  l=l+1;m=m+1;
	}
	else if(ar[j][k]=='0'){
	  l=l+1;
	}
	
      }
      wp[j]=m/l;
      //  printf("wp %d %f\n",j,wp[j]);
    }

    Rep(j,no){
      double tot=0,tot2=0;
      Rep(k,no){
	if(ar[j][k]!='.'){
	  double a1=0,a2=0;
	  Rep(l,no){
	    if(ar[k][l]=='1' && l != j){
	      a1=a1+1;
	      a2=a2+1;
	    }
	    else if(ar[k][l]=='0' && l!=j){
	      a2=a2+1;
	    }
	  }
	  tot=tot+(a1/a2);
	  tot2=tot2+1;
	  //  printf("%f\n",tot);
	}
      }
      owp[j]=tot/tot2;
      // printf("owp %d %f\n",j,owp[j]);
    }

    Rep(j,no){
      double a1=0,a2=0;
      Rep(k,no){
	if(ar[j][k]=='1' || ar[j][k]=='0'){
	  a1=a1+owp[k];a2=a2+1;
	}
      }
      oowp[j]=a1/a2;
      // printf("oowp %d %f\n",j,oowp[j]);
    }
    printf("Case #%d:\n",i+1);

    Rep(j,no){
      printf("%f\n",0.25*wp[j]+0.50*owp[j]+0.25*oowp[j]);
    }

  }

}
