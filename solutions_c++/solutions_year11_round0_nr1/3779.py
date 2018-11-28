#include <iostream>
#include <fstream>
#include <string.h>
#include <stdio.h>

using namespace std;

ifstream fin;
ofstream fout;
//FILE *fin;

int runCase();

int main(int argc, char** argv){
  if(argc != 2){
    cout << argv[0] << " filename" << endl;
  }
  char filename[50];
  strcpy(filename,argv[1]);
  fin.open(strcat(filename,".in"));
  strcpy(filename,argv[1]);
  fout.open(strcat(filename,".out"));

  //fin=fopen(argv[1],"r");
  if(!fin.is_open()){
    cout << "Could not open the file : " << argv[1] << endl;
    return -1;
  }

  int numCase;
  fin >> numCase;
  //fscanf(fin,"%d",&numCase);
  //cout << "number case : " << numCase << endl;
  int i;
  for(i=0;i<numCase;i++){
    int result=runCase();
    cout << "Case #" << i+1 << ": " << result << endl;
    fout << "Case #" << i+1 << ": " << result << endl;
  }

  fin.close();
  fout.close();
  //fclose(fin);

}

int runCase(){
  int numButton;

  fin >> numButton;
  //fscanf(fin,"%d",&numButton);
  //cout << "Number Button : " << numButton << endl;
  
  int blue[2][100];
  int orange[2][100];
  int i;
  char color;
  int b_index=0;
  int o_index=0;
  int buttonNum;

  for(i=0;i<100;i++){
    blue[0][i]=0;
    blue[1][i]=0;
    orange[0][i]=0;
    orange[1][i]=0;
  }

  for(i=0;i<numButton;i++){
    fin >> color;
    fin >> buttonNum;
    //fscanf(fin,"%s %d",color,&buttonNum);

    //cout << "Color : " << color << " button : " << buttonNum << endl;

    switch(color){
    case 'o':
    case 'O': {
      orange[0][o_index]=i;
      orange[1][o_index++]=buttonNum;
      break;
    }
    case 'b':
    case 'B': {
      blue[0][b_index]=i;
      blue[1][b_index++]=buttonNum;
      break;
    }
    default:
      cout << "Error : " << color << " " << buttonNum << endl;
    }
  }

  int time=0;
  
  int bluePos=1;
  int orangePos=1;
  int b=0;
  int o=0;
  bool orange_push_button=false;
  bool blue_push_button=false;
  while(1){
    time++;
    //cout << time << "\t| ";
    if(o >= o_index){
      //cout << "Stay at button " << orangePos;
    }
    else{
      if(orangePos == orange[1][o]){
	if(b < b_index){
	  if(orange[0][o] < blue[0][b]){
	    //cout << "Push button " << orangePos << "\t";
	    orange_push_button=true;
	    //o++;
	  }
	  else{
	    //cout << "Stay at button " << orangePos;
	  }
	}
	else{
	  //cout << "Push button " << orangePos << "\t";
	  orange_push_button=true;
	}
      }
      else if(orangePos < orange[1][o]){
	orangePos++;
	//cout << "Move to button " << orangePos;
      }
      else if(orangePos > orange[1][o]){
	orangePos--;
	//cout << "Move to button " << orangePos;
      }
    }
    //cout << "\t| ";
    
    if(b >= b_index){
      //cout << "Stay at button " << bluePos;
    }
    else{
      if(bluePos == blue[1][b]){
	if(o<o_index){
	  if(blue[0][b] < orange[0][o]){
	    //cout << "Push button " << bluePos;
	    blue_push_button=true;
	    //b++;
	  }
	  else{
	    //cout << "Stay at button " << bluePos;
	  }
	}
	else{
	  //cout << "Push button " << bluePos;
	  blue_push_button=true;
	}
      }
      else if(bluePos < blue[1][b]){
	bluePos++;
	//cout << "Move to button " << bluePos;
      }
      else if(bluePos > blue[1][b]){
	bluePos--;
	//cout << "Move to button " << bluePos;
      }
    }
    //cout << endl;
    
    if(orange_push_button){
      o++;
      orange_push_button=false;
    }
    if(blue_push_button){
      b++;
      blue_push_button=false;
    }
    if((b==b_index && o==o_index) || time > 10000000){
      return time;
    }
  }

  return -1;
}
