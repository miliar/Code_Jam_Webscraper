#include <iostream>
#include <cstdlib>
#include <vector>
using namespace std;

char get(int i, int j, const vector<string> &v)
{
  int h=v.size();
  if (i<0) return ' ';
  if (i>=h) return ' ';
  if (j<0) return ' ';
  if (j>=v[i].length()) return ' ';
  return v[i][j];
}

int main()
{
  string line;
  getline(cin, line);
  int cases=atoi(line.c_str());
  for (int c=1; c<=cases; c++){
    getline(cin, line);
    int n=atoi(line.c_str());

    vector<string> bd(2*n-1);
    for (int i=0; i<2*n-1; i++)
      getline(cin, bd[i]);

    int min_dist=0x7fffffff;

    for (int i=0; i<2*n-1; i++){
      for (int j=0; j<2*n-1; j++){
	/*
	if (!(get(i, j, bd)!=' ' ||
	      (get(i, j-1, bd)!=' ' && get(i, j+1, bd)!=' ')))
	  continue;
	*/

	int dist=0;
	for (int k=0; k<2*n-1; k++){
	  for (int l=0; l<2*n-1; l++){
	    char c=get(k, l, bd);
	    if (c==' ') continue;
	    char d=get(i+i-k, l, bd);
	    char e=get(k, j+j-l, bd);
	    if (c!=' ' && d!=' ' && c!=d){
	      //cout<<i<<", "<<j<<": "<<k<<", "<<l<<endl;
	      goto _next;
	    }
	    if (c!=' ' && e!=' ' && c!=e){
	      //cout<<i<<", "<<j<<": "<<k<<", "<<l<<endl;
	      goto _next;
	    }
	    dist=max(dist, abs(i-k)+abs(j-l));
	  }
	  }
	//cerr<<"*** "<<i<<", "<<j<<": "<<dist<<endl;
	min_dist=min(min_dist, dist+1);
      _next:;
      }
    }

    //cerr<<min_dist<<endl;

    cout<<"Case #"<<c<<": "<<(min_dist*min_dist-n*n)<<endl;
  }
  
  return 0;
}
