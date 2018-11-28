#include<cstdio>
#include<cstdlib>

int mapping[27];
char *from;
char *to;
int n;
char c;

int main(){
 FILE *fin,*fout;
 fin = fopen("A-small-attempt1.in","r");
 fout = fopen("lang2.out","w");
 from = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvqz0";
 to = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupzq";
 int i;
 for(i=0;from[i]!='0';i++){
  mapping[from[i]-'a']=to[i];
 }
// for(i=0;i<26;i++) printf("%c: %c\n",i+'a',mapping[i]);
 
 fscanf(fin,"%d\n",&n);
 for(i=0;i<n;i++){
  fprintf(fout,"Case #%d: ",i+1);
  fscanf(fin,"%c",&c);
  while(c!='\n'){
   if(c==' ') printf(" ");
   fprintf(fout,"%c",mapping[c-'a']);
   fscanf(fin,"%c",&c);
  }
  fprintf(fout,"\n");
 }

 return 0;
}
