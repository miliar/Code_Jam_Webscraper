#include <stdio.h>
#include <assert.h>
#include <string.h>

#include <map>

#define MAX_NAME_SIZE_WITH_NULL_TERMINATE 101
#define MAX_S 100
#define MAX_Q 1000


using namespace std;

struct classcomp {
  bool operator() (const char *s1, const char *s2) const
  {return strcmp(s1,s2) < 0;}
};


int main(int argc, char **argv)
{
  //in vars (help to read files)
  int numOfStances,i,j;
  FILE *fileIn, *fileOut;

  //problem vars
  int s,q;
  char searchEngine[MAX_S][MAX_NAME_SIZE_WITH_NULL_TERMINATE];
  char buffer[MAX_NAME_SIZE_WITH_NULL_TERMINATE];

  if (argc<3){
    printf("You need to especify the input and output files");
    return 0;
  }

  assert(argv[1]);
  assert(argv[2]);

  fileIn  = fopen(argv[1],"r");
  fileOut = fopen(argv[2],"wt");
  if(!fileIn || !fileOut){
    printf("File open problem!!!");
    return 0;
  }

  fscanf(fileIn,"%d",&numOfStances);


  for (i=0;i<numOfStances;++i){

    map<const char*,int,classcomp> findingMap;
    int curFindingMin=0;
    int numOfMinFinding;

    fscanf(fileIn,"%d\n",&s);
    for(j=0;j<s;++j){
      fgets(searchEngine[j],MAX_NAME_SIZE_WITH_NULL_TERMINATE,fileIn);
      findingMap.insert (pair<const char*,int>(searchEngine[j],0));
    }
    numOfMinFinding = s;

    fscanf(fileIn,"%d\n",&q);
    for(j=0;j<q;++j){
      fgets(buffer,MAX_NAME_SIZE_WITH_NULL_TERMINATE,fileIn);

      if(findingMap[buffer] == curFindingMin){

        findingMap[buffer] += 1;

        --numOfMinFinding;

        if(!numOfMinFinding){
          findingMap[buffer] += 1;
          numOfMinFinding = s-1;
          curFindingMin++;
        }
      }
    }

    fprintf(fileOut,"Case #%d: %d",i+1,curFindingMin);
    if(i < numOfStances - 1)
      fprintf(fileOut,"\n");
  }

  fclose(fileIn);
  fclose(fileOut);

  return 0;
}
