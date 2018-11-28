#include<iostream>
using namespace std;

class ext_int{
public:
  int creator;
  char* ind;
  ext_int(){
    creator = 0;
    ind = NULL;
  }
};

int terrain[102][102];
int dir[102][102];
ext_int sink[102][102];

int H = 0, W = 0;

void readdata(){
  H = 0; W = 0;
  cin>>H>>W;

  for(int i = 0; i<= H+1; i ++)
    for(int j = 0; j <= W+1; j++)
      if((i == 0) || (i == H+1) ||(j == 0) ||(j == W+1))
	terrain[i][j] = 12000;
      else cin>>terrain[i][j];

  for(int i = 0; i<= H+1; i ++)
    for(int j = 0; j <= W+1; j++){
      if(sink[i][j].creator){
	sink[i][j].creator = 0;
	delete sink[i][j].ind;
      }
      sink[i][j].ind = NULL;
    }
  /*
  cout<<"testing input"<<endl;
  for(int i = 0; i<= H+1; i ++){
    for(int j = 0; j <= W+1; j++)
      cout<<terrain[i][j];
    cout<<endl;
  }
  cout<<"input ok"<<endl;*/
}
void printdata(){

  for(int i = 1; i<= H; i ++){
    for(int j = 1; j <= W; j++)
      cout<<*(sink[i][j].ind)<<" ";
  cout<<endl;
  }
}

/*

012
345
678

 */
void calcdir(){

  for(int i = 1; i<= H; i ++)
    for(int j = 1; j <= W; j++){
      int ldir = 4;
      int val = terrain[i][j];
      int ind = 0;


      for(int m = -1; m <=1 ; m++)
	for(int  n = -1; n <= 1; n++, ind++){
	  if(m*n == 0)
	    if(val> terrain[i+m][j+n]){
	      val = terrain[i+m][j+n];
	      ldir = ind;
	    }
	}
      
      dir[i][j] = ldir;
    }
  /*  cout<<"dirn"<<endl;
  for(int i = 1; i<= H; i ++){
    for(int j = 1; j <= W; j++)
      cout<<dir[i][j];
    cout<<endl;
  }
  cout<<"dirn ok"<<endl;*/
}



void calcsink(){
  char curr_sink = 'a';
  // cout<<"sinks"<<endl;
  for(int i = 1; i<= H; i ++)
    for(int j = 1; j <= W; j++)
      if(sink[i][j].ind == NULL){
	//	cout<<"here"<<endl;
	int m = i, n = j;
	sink[i][j].ind = new char;
	sink[i][j].creator = 1;

	do{	  
	  sink[m][n].ind = sink[i][j].ind;
	  m = m + dir[m][n]/3 -1;
	  n = n + dir[m][n]%3 -1;
	}	
	while((dir[m][n] != 4) && (sink[m][n].ind == NULL));

	if((m == i)&&(n == j)){	  
	  *(sink[i][j].ind) = curr_sink;
	  curr_sink++;
	}
	else if(sink[m][n].ind != NULL)
	  *(sink[i][j].ind) = *(sink[m][n].ind);
	else{	
	  sink[m][n].ind = sink[i][j].ind;
	  *(sink[i][j].ind) = curr_sink;
	  curr_sink++;
	}
      }
  //  cout<<"end sinks"<<endl;
}

int main(){

  int notest;
  cin>>notest;

  for(int i = 0; i < notest; i ++){
    readdata();
    calcdir();
    calcsink();
    cout<<"Case #"<<(i+1)<<":"<<endl;
    printdata();
    cout<<endl;

  }
}
