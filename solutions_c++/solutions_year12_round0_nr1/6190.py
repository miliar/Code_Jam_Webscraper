# include<iostream>
# include<string>
#include <fstream>


void CharReplace(char &character);

using namespace std;

int main (){
    int i =0;
    int check = 0;
    string Googlerese;
    ifstream myInFile("A-small-attempt2.in");
    ofstream myOutFile("A-small-attempt2.out");
     if (myOutFile.is_open() && myInFile.is_open()){
        //cout<<"Open\n";  
        while ( myInFile.good()){
            getline(myInFile, Googlerese);
            if(check == 0){
                     check =1;
                     continue;
            }
            for(int j = 0;j<Googlerese.size();j++){
                    if(Googlerese[j] == ' '){
                            continue;                 
                    }
                    CharReplace(Googlerese[j]);
            }
            i++;
            myOutFile<<"Case #"<<i<<": "<<Googlerese<<endl;
            
        }
        myInFile.close();
        myOutFile.close(); 
        return 0;                   
     } else {
         //cout<<"Not opened\n";       
         return 0;
     }  
}

void CharReplace(char &character){
     switch(character){
         case 'a':
              character = 'y';
              break;
          case 'b':
              character = 'h';
              break;
           case 'c':
              character = 'e';
              break; 
           case 'd':
              character = 's';
              break;
           case 'e':
              character = 'o';
              break;
           case 'f':
              character = 'c';
              break;
           case 'g':
              character = 'v';
              break;
            case 'h':
              character = 'x';
              break;
            case 'i':
              character = 'd';
              break;
             case 'j':
              character = 'u';
              break;
            case 'k':
              character = 'i';
              break;
             case 'l':
              character = 'g';
              break;
            case 'm':
              character = 'l';
              break;
            case 'n':
              character = 'b';
              break;
            case 'o':
              character = 'k';
              break;
            case 'p':
              character = 'r';
              break;
            case 'q':
              character = 'z';
              break;
            case 'r':
              character = 't';
              break; 
            case 's':
              character = 'n';
              break;
             case 't':
              character = 'w';
              break;
             case 'u':
              character = 'j';
              break;
             case 'v':
              character = 'p';
              break; 
            case 'w':
              character = 'f';
              break;
             case 'x':
              character = 'm';
              break;
             case 'y':
              character = 'a';
              break;
             case 'z':
              character = 'q';
              break; 
     }     
}
