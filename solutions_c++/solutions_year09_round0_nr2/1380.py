#include <iostream>
#include <cassert>

#define All(v) (v).begin(),(v).end()
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x))

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)

using namespace std;

static void solve_case(int i);

int main(void){

	int N;
	cin >> N;
	for(int i = 0; i < N; i++){
		solve_case(i+1);
	}

	return 0;
}
int H,W;

const int MAX_H = 100;
const int MAX_W = 100;

int  input[MAX_H][MAX_W];
char output[MAX_H][MAX_W];

int reg_cnt = 0;

struct dirs{
    int dx, dy;
};

char stack[MAX_W*MAX_H];
int top;

dirs D[4] = { {-1,0}, {0,-1}, {0,1},  {1,0}  };

void flood(int i, int j)
{
    assert(output[i][j] == 0);

    char region = 'a' + reg_cnt;
    top = 0;

    while(true){
	output[i][j] = region;

	int dd[4];
	int vd[4];
	int id = 0;

	REP(k,4){
	    int ni = i + D[k].dx;
	    int nj = j + D[k].dy;
	    if( (ni >= 0) && ( ni < H )  && (nj >= 0) && (nj < W) ){
		    dd[id] = k;
		    vd[id] = input[ni][nj];
		    id++;
		}
        }
	
	REP(k,id){
	    REP(l,k){
		if(vd[k] < vd[l]){
		    swap(vd[k],vd[l]);
		    swap(dd[k],dd[l]);
		}
	    }
	}

	if(id > 0 && vd[0] < input[i][j]){
	    
	    stack[top++] = dd[0];
	    int ni = i + D[dd[0]].dx;
	    int nj = j + D[dd[0]].dy;


	    if(output[ni][nj] != 0){
		int label = output[ni][nj];

		for(int u = top-1; u >= 0; u--){ 
		    ni -= D[stack[u]].dx;
		    nj -= D[stack[u]].dy;
			
		    assert(output[ni][nj] == region);
		    output[ni][nj] = label;
		    
		}
		break;
	    } else {
		i = ni;
		j = nj;
		
	    } 
	} else {
	    reg_cnt++;
	    break;
	}

	}
}

void solve_case(int cn){
    cin >> H >> W;

    REP(i,H){
	REP(j,W){
	    int x;
	    cin >> x;
	    input[i][j] = x;
	    output[i][j] = 0;
	}
    }

    reg_cnt = 0;
    top = 0;
    cout << "Case #" << cn << ":" << endl;
    REP(i,H){
	REP(j,W){
	    if(output[i][j] == 0)
		flood(i,j);
	}
    }

    REP(i,H){
	REP(j,W-1){
	    cout << output[i][j] << " ";
	}
	cout << output[i][W-1] << endl;
    }

}
