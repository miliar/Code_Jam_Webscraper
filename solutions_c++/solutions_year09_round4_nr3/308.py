#include <iostream>
#include <vector>
using namespace std;

int cur_ans;

int paint(int cur, int col, vector<int> &hist, vector<vector<bool> > &g)
{
  int n=g.size();

  if (col>=cur_ans) return cur_ans;

  if (cur==n){
    cur_ans=min(cur_ans, col);
    return col;
  }
  int ret=9999;

  for (int c=0;c<=col;c++){
    bool ok=true;
    for (int i=0;i<cur;i++){
      if (g[i][cur]&&hist[i]==c){
	ok=false;
	break;
      }
    }
    if (!ok) continue;
    hist[cur]=c;
    ret=min(ret, paint(cur+1, max(c+1, col), hist, g));
  }
  return ret;
}

int main()
{
  int cases; cin>>cases;
  for (int c=1; c<=cases; c++){
    int n, k; cin>>n>>k;
    vector<vector<int> > ch(n, vector<int>(k));
    for (int i=0;i<n;i++)
      for (int j=0;j<k;j++)
	cin>>ch[i][j];
    vector<vector<bool> > g(n, vector<bool>(n));
    for (int i=0;i<n;i++){
      for (int j=i+1;j<n;j++){
	bool f=false;
	for (int l=0;l<k-1;l++){
	  if (ch[i][l]==ch[j][l]||
	      ch[i][l+1]==ch[j][l+1]||
	      ch[i][l]<ch[j][l]&&ch[i][l+1]>ch[j][l+1]||
	      ch[i][l]>ch[j][l]&&ch[i][l+1]<ch[j][l+1])
	    f=true;
	}
	g[i][j]=f;
	g[j][i]=f;
      }
    }
    vector<int> hist(n, -1);
    cur_ans=9999;
    cout<<"Case #"<<c<<": "<<paint(0,0,hist,g)<<endl;
  }
  return 0;
}
