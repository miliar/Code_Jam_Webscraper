#include <stdio.h>
#include <conio.h>


int length, wordLength, patternLength;

char words[5000][20];

char patterns[500][320];



int checkWord(int word, int pattern);
int checkPattern(int pattern);
int checkLetter(char letter, int pattern, int patternLetter);


int main(){
     FILE *fileIn, *fileOut;
	fileIn=fopen("C:\\GCJ\\Q\\A-large.in", "r");
	fileOut=fopen("C:\\GCJ\\Q\\A-large.out", "w");
	if (fileIn!=NULL) {
     
        
        fscanf(fileIn,"%d %d %d\n",&length,&wordLength,&patternLength);

        for (int iWord=0;iWord<wordLength;iWord++){
            fscanf(fileIn,"%s\n",words[iWord]);
        }
        
        for (int iPattern=0;iPattern<patternLength;iPattern++){
            fscanf(fileIn,"%s\n",patterns[iPattern]);
            int result = checkPattern(iPattern);
            fprintf(fileOut,"Case #%d: %d\n",iPattern+1,result); 
        }
    }
    fclose(fileIn);
    fclose(fileOut);
    return 0;  
}


int checkWord(int word, int pattern){
    int wordMatch = 1;
    int iCurrentLetter = 0;
    int currentLetterInPattern=0;
    while (iCurrentLetter<length && wordMatch==1){
          int log = 1;
        currentLetterInPattern = checkLetter(words[word][iCurrentLetter], pattern,currentLetterInPattern);
        if (currentLetterInPattern==-1)
           wordMatch = 0; 
        iCurrentLetter++;
    }
    return wordMatch;
}

int checkLetter(char letter, int pattern, int patternLetter){
    int result = -1;
    if (patterns[pattern][patternLetter]=='('){
       int res = 0;
       do {
           patternLetter++;
           if (patterns[pattern][patternLetter]==letter)
              res = 1;
       }while (patterns[pattern][patternLetter]!=')');
       if (res == 1){
          result = patternLetter+1;
       }
    }else if (patterns[pattern][patternLetter]==letter){
          result =  patternLetter+1;
    }
    return result;
    
}

int checkPattern(int pattern){
    int numWords = 0;
    for (int i=0;i<wordLength;i++){
        numWords = numWords + checkWord(i,pattern);
    }
    return numWords;
}
