#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <string>
#include <vector>

using namespace std;


struct Sink{
    int x ;
    int y;
} ;

bool exist(int x, int y, struct Sink flow[][101*101], int _m, int _n ,int &ret_x, int &ret_y) 
{
    for(int _i = 0; _i < _m; _i++ ) {
	for(int _j = 0; _j < _n; _j++) {
	    if(x == flow[_i][_j].x &&  y == flow[_i][_j].y) {
		ret_x = _i;
		for(;_j < _n; _j++) {
		    if(flow[_i][_j].x == 0) {
			ret_y = _j;
			return true;
		    }
		}
	    } 
	}
    }
    return false;
}

struct Sink mini(int **map, int i, int j)
{
    int mix = map[i][j];
    struct Sink sink;
    sink.x = i;
    sink.y = j;
   if(map[i-1][j] < mix) {
       mix = map[i-1][j];
       sink.x = i-1;
       sink.y = j;
   }
   if(map[i][j-1] < mix) {
       mix = map[i][j-1];
       sink.x = i;
       sink.y = j-1;
   }
   if(map[i][j+1] < mix) {
       mix = map[i][j+1];
       sink.x = i;
       sink.y = j+1;
   }
   if(map[i+1][j] < mix) {
       mix = map[i+1][j];
       sink.x = i+1;
       sink.y = j;
   }
   return sink;
   
}
char** waitershad(int **map,int r,int c)
{
    char ** ret = new char*[r-2];
    for(int i = 0; i < r-2; i++) {
	ret[i] = new char[c-2+1];
	memset(ret[i],'\0',c-2+1);
    }
    struct Sink flow[26][101*101];
    for(int i = 0; i < 26; i++) {
	for(int j = 0; j < 101*101; j++) {
	    flow[i][j].x = 0;
	    flow[i][j].y = 0;
	}
    }
    int _m = 0;
    for(int _m1= 0; _m1 < (r-2)*(c-2); _m1++) {
	int _n = 0;
	int m=0,n=0;
	int flag = 0;
	struct Sink tmp_flow[101*101];
	for(int i = 0; i < 101*101; i++) {
	    tmp_flow[i].x = 0;
	    tmp_flow[i].y = 0;
	}
	for(int i = 1; i < r-1; i++) {
	    for(int j = 1; j < c-1; j++) {
		if(_n == 0 || (i == m && j == n)) {
		    int ret_x = -1;
		    int ret_y = -1;
		    if(true == exist(i,j,flow,26,101*101,ret_x, ret_y)) {
			if(_n == 0) {
			    continue;
			}
			for(int i = 0; i < _n; i++) {
			    flow[ret_x][ret_y+i] = tmp_flow[i];
			}
			flag = 1;
			break;
		    }
		    struct Sink sink = mini(map,i,j);
		    struct Sink tmp;
		    tmp.x = i;
		    tmp.y = j;
		    if(sink.x == i && sink.y == j ) {
			int i = 0;
			for(i = 0; i < _n; i++ ) {
			    flow[_m][i] = tmp_flow[i];
			}
			flow[_m][i] = sink;
			flag = 1;
			_m++;
			break;
		    } else {
			tmp_flow[_n] = tmp; 
			_n++;
			/*
			if(true == exist(sink.x,sink.y,flow,26,101*101,ret_x,ret_y)) {
			    for(int i = 0; i < _n; i++) {
				flow[ret_x][ret_y+i] = tmp_flow[i];
			    }
			    flag = 1;
			    break;
			} else {
			    tmp_flow[_n] = sink;
			*/
			    m = sink.x;
			    n = sink.y;
			    i = 1;
			    j = 1;
			//}
			    if(true == exist(sink.x,sink.y,flow,26,101*101,ret_x,ret_y)) {
				for(int i = 0; i < _n; i++) {
				    flow[ret_x][ret_y+i] = tmp_flow[i];
				}
				flag = 1;
				break;
			    }

		    }
		}
	    }
	    if(flag == 1) {
		break;
	    }
	}
    }
    for(int i = 0; i < 26; i++) {
	for(int j = 0; j < 101*101; j ++) {
	    if(0 == flow[i][j].x) {
		break;
	    }
	    ret[flow[i][j].x-1][flow[i][j].y-1] = 'a'+i;
	}
    }
    return ret;
}

int main()
{
    FILE *fp;
    fp = fopen("./a1.txt","r");
    if(fp == NULL){
	return 0;
    }
    char buf[1024];
    memset(buf,'\0',1024);
    int row = 0;
    int caseid = 0;
    int casenum = 0;
    while(fgets(buf,1024,fp)) {
	if(row == 0) {
	    casenum = atoi(buf);
	    row++;
	    continue;
	}
	char *p = strchr(buf,' ');
	*p = 0;
	int r = atoi(buf)+2;
	int c = atoi(p+1)+2;
	int ** map = new int*[r];
	for(int i = 0; i < r; i++) {
	    map[i] = new int[c];
	}
	for(int i = 0; i < c; i++) {
	    map[0][i] = 10001;
	    map[r-1][i] = 10001;
	}
	for(int i = 0; i < r; i++) {
	    map[i][0] = 10001;
	    map[i][c-1] = 10001;
	}
	for(int i = 1; i < r-1; i++) {
	    char tmp[1024];
	    memset(tmp, 0, 1024);
	    char *p1 = NULL;
	    char *p2 = NULL;
	    fgets(tmp,1024,fp);
	    p2 = tmp;
	    for(int j = 1; j < c-1;j++) {
		p1 = strchr(p2,' ');
		if(p1 == NULL) {
		    map[i][j] = atoi(p2);
		    break;
		}
		*p1 = 0;
		map[i][j] = atoi(p2);
		p2 = p1+1;
	    }
	}
	caseid++;
	char** ret = waitershad(map,r,c);
	printf("Case #%d:\n", caseid);
	for(int i = 0; i < r-2; i++) {
	    for(int j = 0; j < c-2; j++) {
		if(j == c-2-1) {
		    printf("%c\n",ret[i][j]);
		} else {
		    printf("%c ",ret[i][j]);
		}
	    }
	    delete ret[i];
	}
	delete ret;
	for(int i = 0; i < r; i++) {
	    delete map[i];
	}
	delete map;

    }
    fclose(fp);
    return 0;
}
 
