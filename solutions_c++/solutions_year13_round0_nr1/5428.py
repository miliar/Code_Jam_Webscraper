#include<stdio.h>

struct vect{
char s[4][4];
};

int gol(char s[4][4])
{
    int i,j,nr=0;
    for (i=0;i<4;i++){
       for (j=0;j<4;j++){
           if (s[i][j]=='.'){nr=1;break;}
       }
    }
    if (nr==1) return 1;
    else return 0;
}

int coloana(char s[4][4],char c)
{
int i,j,nr;
  for (i=0;i<4;i++){
    nr=0;
    for (j=0;j<4;j++){
        if ((s[j][i]==c) || (s[j][i]=='T')) nr=nr+1;
    }
    if (nr==4) break;
  }
  if (nr==4) return 1;
  else return 0;
}

int diagonala(char s[4][4],char c)
{
int i,j,nr=0;
  for (i=0;i<4;i++){
    if ((s[i][i]==c) || (s[i][i]=='T')) nr=nr+1;
  }
  if (nr==4) return 1;
  nr=0;
  for (i=0;i<4;i++){
    if ((s[i][4-i-1]==c) || (s[i][4-i-1]=='T')) nr=nr+1;
  }
  if (nr==4) return 1;
  else return 0;
}


int linie(char s[4][4],char c)
{
int i,j,nr;
  for (i=0;i<4;i++){
    nr=0;
    for (j=0;j<4;j++){
        if ((s[i][j]==c) || (s[i][j]=='T')) nr=nr+1;
    }
    if (nr==4) break;
  }
  if (nr==4) return 1;
  else return 0;
}


int main()
{
    FILE *f,*fo;
    f=fopen("input.txt","r");
    fo=fopen("output.txt","w");

    int n,j,k;
    vect v[10];
    char a[5],b[5],c[5],d[5];
    fscanf(f,"%d",&n);
    int i;
   // printf("%d\n",n);
    for (i=0;i<n;i++){
        fscanf(f," %s",&a);
      //  printf("%s\n",a);
        fscanf(f," %s",&b);
       // printf("%s\n",b);
        fscanf(f," %s",&c);
       // printf("%s\n",c);
        fscanf(f," %s",&d);
      //  printf("%s\n",d);

        v[i].s[0][0]=a[0];
        v[i].s[0][1]=a[1];
        v[i].s[0][2]=a[2];
        v[i].s[0][3]=a[3];

        v[i].s[1][0]=b[0];
        v[i].s[1][1]=b[1];
        v[i].s[1][2]=b[2];
        v[i].s[1][3]=b[3];

        v[i].s[2][0]=c[0];
        v[i].s[2][1]=c[1];
        v[i].s[2][2]=c[2];
        v[i].s[2][3]=c[3];

        v[i].s[3][0]=d[0];
        v[i].s[3][1]=d[1];
        v[i].s[3][2]=d[2];
        v[i].s[3][3]=d[3];
    }
    int verif=0;
    for (i=0;i<n;i++){
        verif=0;
        if (linie(v[i].s,'X')==1) {fprintf(fo,"Case #%d: X won\n",i+1);continue;}
        if (linie(v[i].s,'O')==1) {fprintf(fo,"Case #%d: O won\n",i+1);continue;}

        if (coloana(v[i].s,'X')==1) {fprintf(fo,"Case #%d: X won\n",i+1);continue;}
        if (coloana(v[i].s,'O')==1) {fprintf(fo,"Case #%d: O won\n",i+1);continue;}

        if (diagonala(v[i].s,'x')==1) {fprintf(fo,"Case #%d: X won\n",i+1);continue;}
        if (diagonala(v[i].s,'O')==1) {fprintf(fo,"Case #%d: O won\n",i+1);continue;}

        if (gol(v[i].s)==0) fprintf(fo,"Case #%d: Draw\n",i+1);
        else fprintf(fo,"Case #%d: Game has not completed\n",i+1);
    }
}
