#include<stdio.h>
#include<string.h>
#include<conio.h>

typedef struct directory{
  char name[101];
  directory *subDirs;
  int subCount;
}directory;


int addDir(directory &dir,char* newDir){
  char dirName[100];
  int h,pos;
  for(pos=0;newDir[pos]!='/' && newDir[pos]!='\0';pos++)
    dirName[pos]=newDir[pos];     
  dirName[pos]='\0';
  
  
  for(h=0;h<dir.subCount;h++){
    if(!strcmp(dir.subDirs[h].name,dirName)){
      if(newDir[pos]=='/')
        return addDir(dir.subDirs[h],newDir+pos+1);
      return 0;
    }
  }
  
  dir.subCount++;
  directory *tmp=new directory[dir.subCount];
  for(h=0;h<dir.subCount-1;h++){
    strcpy(tmp[h].name,dir.subDirs[h].name);
    tmp[h].subDirs=dir.subDirs[h].subDirs;
    tmp[h].subCount=dir.subDirs[h].subCount;
  }
  dir.subDirs=tmp;
  strcpy(dir.subDirs[dir.subCount-1].name,dirName);
  dir.subDirs[dir.subCount-1].subCount=0;
  if(newDir[pos]=='/')
    return 1+addDir(dir.subDirs[dir.subCount-1],newDir+pos+1);
  return 1;
}

int main(){
  FILE *fin;
  FILE *fout;
  int numberOfInputs;
  fin=fopen("D:\\task.in","r");
  fout=fopen("D:\\task.out","w");  
  fscanf(fin,"%d\n",&numberOfInputs);
  
  int N,M,count; 
  char newDir[101];
  for(int h=0;h<numberOfInputs;h++){
    directory root;
    strcpy(root.name,"ROOT");
    root.subCount=0;
    fscanf(fin,"%d %d\n",&N,&M);
    
    for(int x=0;x<N;x++){
      fscanf(fin,"%s\n",newDir);
      addDir(root,newDir+1);        
    } 
    
    count=0;
    for(int x=0;x<M;x++){
      fscanf(fin,"%s\n",newDir);
      count+=addDir(root,newDir+1);        
    } 
    
    fprintf(fout,"Case #%d: %d\n",h+1,count);
  }
  
  //Global things
  fclose(fin);
  fclose(fout);   
}
