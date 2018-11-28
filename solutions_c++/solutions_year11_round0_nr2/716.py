#include <iostream>
#include <string>

#define C 36
#define D 28
#define N 100

using namespace std;

int main(){
  int case_num,i, j, k,comb_num,oppose_num,input_num, output_num, comb_f, oppose_f;
  char comb[3][C], oppose[2][D], input[N], output[N];
  cin >> case_num;
  for(j=0; j<case_num ; j++){
    //combine
    cin >> comb_num;
    for(i=0; i<comb_num; i++){
      for(k=0; k<3; k++){
	cin >> comb[k][i];
      }
    }
    //oppose
    cin >> oppose_num;
    for(i=0; i<oppose_num; i++){
      for(k=0; k<2;k++){
	cin >> oppose[k][i];
      }
    }
    //input
    cin >> input_num;
    for(i=0; i<input_num; i++){
      cin >> input[i];
    }
    
    output_num=0;
    output[0]=input[0];
    for(i=0;i<input_num;i++){
      comb_f=0;
      oppose_f=0;
      //アウトプットの末尾とインプットが合成を起こすかチェック
      if(output_num!=0){//if there is something in the list
	int s,t, u;
	for(t=0; t< comb_num; t++){
	  for(s=0; s<2; s++){
	    if(output[output_num-1]==comb[s][t] && input[i]==comb[1-s][t]){
	      output[output_num-1] = comb[2][t];//末端の番号は変わらない
	      //cout << "c to " << comb[2][t] << endl;
	      comb_f=1;
	    }
	  }
	}
	//消滅を起こすかチェック
	if(comb_f!=1){
          output[output_num]=input[i];
          output_num++;
	  
	  for (k=0; k< oppose_num ;k++){
	    for(t=0; t< output_num; t++){
	      for(u=0; u<t;u++){
		for(s=0; s<2; s++){
		  if(output[t]==oppose[s][k] && output[u]==oppose[1-s][k]){
		    output_num=0;
		    oppose_f=1;
		    //cout << "d: " << oppose[s][k] << "&" << oppose[1-s][k] << endl;
		  }
		}
	      }
	    }
	  }
	}
	//add char
	/*
	if(comb_f!=1 && oppose_f!=1){
   	  output[output_num]=input[i];
	  output_num++;
	}
	*/
      }else{
	output[output_num]=input[i];
	output_num++;
      }
      
    }
     
    cout <<endl<< "Case #" << j+1 << ": [";
    if(output_num!=0)cout << output[0];
    for(i=1; i<output_num ;i++){
      cout << ", " <<output[i];
    }
    cout << "]" ;
  }//one case
  cout << endl;
  return 0;
}

