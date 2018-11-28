#include <cstdio>
#include <vector>
#include <cstring>

using namespace std;

int T,N,C,D;

int opposed[256][256];
int combine[256][256];
int present[256];

char buf[256];

vector<char> out;

int main(){
  scanf("%d", &T);

  for (int ttt=1; ttt<=T; ttt++){
    memset(opposed, 0, sizeof opposed);
    memset(combine, 0, sizeof combine);
    memset(present, 0, sizeof present);
    out.clear();
    scanf("%d", &C);
    for (int i=0; i<C; i++){
      scanf("%s", buf);
      combine[buf[0]][buf[1]]=combine[buf[1]][buf[0]]=buf[2];
    }
    scanf("%d", &D);
    for (int i=0; i<D; i++){
      scanf("%s", buf);
      opposed[buf[0]][buf[1]]=opposed[buf[1]][buf[0]]=1;
    }
    scanf("%d %s", &N, buf);
    for (int i=0; i<N; i++){
      if (out.empty()){out.push_back(buf[i]); present[buf[i]]++; continue;}
      if (combine[out.back()][buf[i]]){
	present[out.back()]--;
	out.back() = combine[out.back()][buf[i]];
	continue;
      }
      else{
	out.push_back(buf[i]);
	present[buf[i]]++;
	for (int j='A'; j<='Z'; j++)
	  if (present[j] && opposed[buf[i]][j]){
	    memset(present,0,sizeof present);
	    out.clear();
	  }
      }
    }
    printf("Case #%d: [", ttt);
    if (out.empty())
      printf("]\n");
    else{
      printf("%c", out.front());
      for(int i=1; i<out.size(); i++)
	printf(", %c", out[i]);
      printf("]\n");
    }
  }
}

