#include <iostream>
#include <cstring>

using namespace std;

unsigned int map[200][200];
int fill_[200][200];
int count_;
int direct[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int check(int a, int b){
    if(fill_[a][b] != -1)
        return fill_[a][b];
    else{
        int small, dir;
	dir = -1;
	small = map[a][b];
	for(int i = 0; i < 4; i++)
 	    if(map[a+direct[i][0]][b+direct[i][1]] < small){
	        dir = i;
	        small = map[a+direct[i][0]][b+direct[i][1]];
	    }

	if(dir == -1){
	    fill_[a][b] = count_;	
	    return count_++;
	}
        else{
	    fill_[a][b] = check(a+direct[dir][0], b+direct[dir][1]);
	    return fill_[a][b];
	}	
    }	    
}

int main(){

    int H, W;
    int cases, c;
    cin >> cases;
    c = cases;
    while(cases--){

        cin >> H >> W;
        memset(map, -1, sizeof(map));
	memset(fill_, -1, sizeof(fill_));
	for(int i = 1; i <= H; i++)
            for(int j = 1; j <= W; j++)
	        cin >> map[i][j];
 
	count_ = 0;
	for(int i = 1; i <= H; i++)
            for(int j = 1; j <= W; j++)
                check(i, j);            
	    
        cout << "Case #" << c-cases << ":\n";

       for(int i = 1; i <= H; i++){
            printf("%c", fill_[i][1]+'a' ); 
	    for(int j = 2; j <= W; j++)
		   printf(" %c", fill_[i][j]+'a' ); 
	    cout << '\n';
       }
    }

    return 0;	
}
