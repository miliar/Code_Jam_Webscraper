#include<conio.h>
#include<stdio.h>
#include<math.h>


int main(int argc, char *argv[])
{
FILE* fichier1 = NULL;
fichier1 = fopen("A-large.in", "r+");

FILE* fichier2 = NULL;
fichier2 = fopen("A-small-attempt.out", "w+");

int test=0;
int c=0;
int x_v=0;
int x_h=0;
int o_v=0;
int o_h=0;
int i=0;
int j=0 ,r=0;
char t[4][4];
int x=0;
int o=0;
int x2=0;
int o2=0;

       fscanf(fichier1,"%d",&test);

                                           fgetc(fichier1);


       for( r=0;r<test;r++)
       {
              x_v=0;
              x_h=0;
              o_v=0;
              o_h=0;
              c=0;
              x=0;
                o=0;
                x2=0;
                o2=0;
               for( i=0; i<4;i++)
               {
                       for(j=0; j<4;j++)
                       {

                            t[i][j]=fgetc(fichier1);
                                           }

                                           fgetc(fichier1);

             }


               for( i=0; i<4;i++)
               {

                       x_h=0;
                        o_h=0;
                        x_v=0;
                        o_v=0;
                       for( j=0; j<4;j++)
                       {
                               if(t[i][j]=='.')
                               {
                                         c=1;
                                }


                            if(t[i][j]=='T')
                            {

                                   x_h++;
                                    o_h++;
                            }



                            if(t[j][i]=='T')
                            {

                                   x_v++;
                                    o_v++;
                            }


                             if(t[i][j]=='X' )
                           {
                                           x_h++;
                                           o_h=0;

                                           }
                           else if(t[i][j]=='O' )
                           {
                                           o_h++;
                                           x_h=0;

                                           }



                           if(t[j][i]=='X' )
                           {
                                           x_v++;
                                           o_v=0;

                                           }
                           else if(t[j][i]=='O' )
                           {
                                           o_v++;
                                           x_v=0;

                                           }

                            if(i==j )
                            {


                                            if(t[i][j]=='T')
                                        {

                                                x++;
                                                o++;
                                        }
                                                 if(t[j][i]=='X' )
                                       {
                                                       x++;
                                                       o=0;

                                                       }
                                       else if(t[j][i]=='O' )
                                       {
                                                       o++;
                                                       x=0;

                                                       }
                            }


                              if((i+j)==3 )
                            {


                                            if(t[i][j]=='T')
                                        {

                                                x2++;
                                                o2++;
                                        }
                                                 if(t[i][j]=='X' )
                                       {
                                                       x2++;
                                                       o2=0;

                                                       }
                                       else if(t[i][j]=='O' )
                                       {
                                                       o2++;
                                                       x2=0;

                                                       }
                            }

                            if(x_h==4 || o_h==4 || x_v==4 || o_v==4 || x==4 || o==4|| x2==4 || o2==4)
                               {
                               break;

                                 }
                            }








                        if(x_h==4 || o_h==4 || x_v==4 || o_v==4 || x==4 || o==4|| x2==4 || o2==4)
                               {
                               break;

                                 }

 }





               if(x_h==4 || x_v==4 || x==4 || x2==4)
               {
                         fprintf(fichier2,"Case #%d: X won\n",r+1);
                         }

               else if(o_h==4 || o_v==4 || o==4 ||o2==4)
               {
                         fprintf(fichier2,"Case #%d: O won\n",r+1);
                         }

               else if(c==1)
               {
                    fprintf(fichier2,"Case #%d: Game has not completed\n",r+1);
                    }

                else
                {

                     fprintf(fichier2,"Case #%d: Draw\n",r+1);
                }


                                           fgetc(fichier1);



         }


return 0;
}
