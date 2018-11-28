#include <stdio.h>
#define NMAX 200


struct ora{
  int hPlecare,minPlecare,hSosire,minSosire;
  };

struct ora_plecare{
  int h,min;
  };


ora_plecare tren_a[NMAX],tren_b[NMAX],minim1,minim2,minim;
ora a[NMAX],b[NMAX];
char mesaj[20];
int nr_teste,contor,timp_intoarcere,plecari_a,plecari_b,i,na,nb,ultima_ora,ultimul_min;
int trenuri_in_a,trenuri_in_b,verif,v1[NMAX],v2[NMAX],j,pozitie1,pozitie2,pozitie;



int main()
 {FILE *f,*g;


  f=fopen("tren.in","r");
  g=fopen("tren.out","w");

  fscanf(f,"%d\n",&nr_teste);
  for (contor=1;contor<=nr_teste;contor++)
     {

      fscanf(f,"%d\n",&timp_intoarcere);
      fscanf(f,"%d %d\n",&plecari_a,&plecari_b);
      for (i=1;i<=plecari_a;i++)
           {fgets(mesaj,20,f);
            a[i].hPlecare=(mesaj[0]-'0')*10+(mesaj[1]-'0');
            a[i].minPlecare=(mesaj[3]-'0')*10+(mesaj[4]-'0');
            a[i].hSosire=(mesaj[6]-'0')*10+(mesaj[7]-'0');
            a[i].minSosire=(mesaj[9]-'0')*10+(mesaj[10]-'0');
            }
      for (i=1;i<=plecari_b;i++)
           {fgets(mesaj,20,f);
            b[i].hPlecare=(mesaj[0]-'0')*10+(mesaj[1]-'0');
            b[i].minPlecare=(mesaj[3]-'0')*10+(mesaj[4]-'0');
            b[i].hSosire=(mesaj[6]-'0')*10+(mesaj[7]-'0');
            b[i].minSosire=(mesaj[9]-'0')*10+(mesaj[10]-'0');
            }


     na=nb=0;
     trenuri_in_a=0;
     trenuri_in_b=0;
     verif=0;



     for (i=1;i<=plecari_a;i++) v1[i]=0;
     for (i=1;i<=plecari_b;i++) v2[i]=0;

     for (i=1;i<=plecari_a+plecari_b;i++)
         {//trebuie sa calculam minimul din plecari cu ora si min
          //mai mari decat ultima_ora si ultimul_min si o retinem in minim
          minim1.h=minim2.h=24;
          minim1.min=minim2.min=60;
          for (j=1;j<=plecari_a;j++)
             if ((verif==0)&&(v1[j]==0))
                           {verif=1;
                            minim1.h=a[j].hPlecare;
                            minim1.min=a[j].minPlecare;
                            pozitie1=j;
                            }
                      else
                if ((minim1.h*60+minim1.min>=a[j].hPlecare*60+a[j].minPlecare)&&(v1[j]==0))
                                        {minim1.h=a[j].hPlecare;
                                         minim1.min=a[j].minPlecare;
                                         pozitie1=j;
                                         }
          verif=0;
          for (j=1;j<=plecari_b;j++)
             if ((verif==0)&&(v2[j]==0))
                           {verif=1;
                            minim2.h=b[j].hPlecare;
                            minim2.min=b[j].minPlecare;
                            pozitie2=j;
                            }
                      else
                if ((minim2.h*60+minim2.min>=b[j].hPlecare*60+b[j].minPlecare)&&(v2[j]==0))
                                        {minim2.h=b[j].hPlecare;
                                         minim2.min=b[j].minPlecare;
                                         pozitie2=j;
                                         }

          //vedem din ce gara pleaca urmatorul tren in functie de minim
          //daca e minim1 pleaca din a
          //altfel pleaca din b
          if (minim1.h*60+minim1.min<minim2.h*60+minim2.min)
                             {//stim ca urmatorul tren pleaca din a
                              //vedem daca avem vreun tren in a care poate pleca
                              //daca avem il ducem in b
                              //altfel mai adaugam un tren la na
                              v1[pozitie1]=1;//am rezolvat trenul de pe pozitia pozitie1
                              //acum ar trebui sa gasesc cel mai mic tren din tren_a astfel incat
                              //acesta sa poata sa plece
                              //pentru asta mai folosesc si minim3
                              //de fapt in tren_a retin orele la care mai pot pleca trenuri din a
                              //deci daca gasesc unul care poate pleca e ok
                              verif=0;
                              for (j=1;j<=trenuri_in_a;j++)
                                  if ((verif==0)&&(tren_a[j].h*60+tren_a[j].min<=minim1.h*60+minim1.min))
                                           {
                                            pozitie=j;
                                            verif=1;
                                            j=trenuri_in_a+1;
                                            }
                              if (verif==0)//adica nu am gsit nici un tren care poate sa plece
                                      {//adaugam noi unul
                                       na++;
                                       trenuri_in_b++;
                                       tren_b[trenuri_in_b].h=a[pozitie1].hSosire;
                                       tren_b[trenuri_in_b].min=a[pozitie1].minSosire+timp_intoarcere;
                                       if (tren_b[trenuri_in_b].min>=60) {tren_b[trenuri_in_b].h+=tren_b[trenuri_in_b].min/60;
                                                                          tren_b[trenuri_in_b].min=tren_b[trenuri_in_b].min%60;
                                                                          }
                                       }
                                    else {//am gasit unul si il ducem in b si il stergem din a
                                          trenuri_in_b++;
                                          tren_b[trenuri_in_b].h=a[pozitie1].hSosire;
                                          tren_b[trenuri_in_b].min=a[pozitie1].minSosire+timp_intoarcere;
                                          if (tren_b[trenuri_in_b].min>=60) {tren_b[trenuri_in_b].h+=tren_b[trenuri_in_b].min/60;
                                                                             tren_b[trenuri_in_b].min=tren_b[trenuri_in_b].min%60;
                                                                             }
                                          for (j=pozitie;j<trenuri_in_a;j++)
                                              {tren_a[j].h=tren_a[j+1].h;
                                               tren_a[j].min=tren_a[j+1].min;
                                               }
                                          trenuri_in_a--;

                                          }
                              }
          //acum facem aceeasi chestie in cazul in care urmatorul tren pleaca din b
          //si poate nu o sa gresesc nici o variabila cand o schimb
                       else  {//stim ca urmatorul tren pleaca din b
                              //vedem daca avem vreun tren in b care poate pleca
                              //daca avem il ducem in a
                              //altfel mai adaugam un tren la nb
                              v2[pozitie2]=1;//am rezolvat trenul de pe pozitia pozitie2
                              //acum ar trebui sa gasesc cel mai mic tren din tren_b astfel incat
                              //acesta sa poata sa plece
                              //pentru asta mai folosesc si minim3
                              //de fapt in tren_a retin orele la care mai pot pleca trenuri din b
                              //deci daca gasesc unul care poate pleca e ok
                              verif=0;
                              for (j=1;j<=trenuri_in_b;j++)
                                  if ((verif==0)&&(tren_b[j].h*60+tren_b[j].min<=minim2.h*60+minim2.min))
                                           {
                                            pozitie=j;
                                            verif=1;
                                            j=trenuri_in_b+1;
                                            }
                              if (verif==0)//adica nu am gsit nici un tren care poate sa plece
                                      {//adaugam noi unul
                                       nb++;
                                       trenuri_in_a++;
                                       tren_a[trenuri_in_a].h=b[pozitie2].hSosire;
                                       tren_a[trenuri_in_a].min=b[pozitie2].minSosire+timp_intoarcere;
                                       if (tren_a[trenuri_in_a].min>=60) {tren_a[trenuri_in_a].h+=tren_a[trenuri_in_a].min/60;
                                                                          tren_a[trenuri_in_a].min=tren_a[trenuri_in_a].min%60;
                                                                          }
                                       }
                                    else {//am gasit unul si il ducem in b si il stergem din a
                                          trenuri_in_a++;
                                          tren_a[trenuri_in_a].h=b[pozitie2].hSosire;
                                          tren_a[trenuri_in_a].min=b[pozitie2].minSosire+timp_intoarcere;
                                          if (tren_a[trenuri_in_a].min>=60) {tren_a[trenuri_in_a].h+=tren_a[trenuri_in_a].min/60;
                                                                             tren_a[trenuri_in_a].min=tren_a[trenuri_in_a].min%60;
                                                                             }
                                          for (j=pozitie;j<trenuri_in_b;j++)
                                              {tren_b[j].h=tren_b[j+1].h;
                                               tren_b[j].min=tren_b[j+1].min;
                                               }
                                          trenuri_in_b--;

                                          }
                              }
          }
       fprintf(g,"Case #%d: %d %d\n",contor,na,nb);

      }


  fclose(f);
  fclose(g);
  return 0;
  }
