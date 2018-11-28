#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector.h>
using namespace std;

int main()
{
    FILE *fd;
    FILE *sortie;
    int nbIteration;
    int i,i2,i3,i4;
    int r,k,n,val;
    int somme=0,place=0;
    vector<int> monvector;

				if((fd=fopen("C-small-attempt1.in","r"))==NULL)//verification de l'ouverture du fichier texte
				{
					printf("Erreur ouverture du fichier\n\n");
				}
				else
				{
                    printf("Lecture OK\n");

					fscanf(fd,"%d",&nbIteration);	//recuperation du Solde du compte
					printf("nombreiteration %d",nbIteration);



					if((sortie=fopen("sortie.out","w"))==NULL)//verification de l'ouverture du fichier texte
                            {
                                printf("Erreur ouverture du fichier\n");
                            }
                            else
                            {
                                    //iteration pour chaque cas
                                    for(i=0;i<nbIteration;i++){
                                        fscanf(fd,"%d %d %d",&r, &k, &n);
                                        monvector.clear();
                                        for(i2=0;i2<n;i2++){

                                            fscanf(fd,"%d",&val);
                                            monvector.push_back(val);
                                        }
                                        somme=0;
                                        //Nombre de tour par jour
                                        for(i2=0;i2<r;i2++){
                                            i3=0;
                                            place=k;
                                            while(place>=monvector.at(0) && i3<=monvector.size()-1){

                                                place=place-monvector.at(0);
                                                somme=somme+monvector.at(0);
                                                monvector.push_back(monvector.at(0));
                                                monvector.erase(monvector.begin());
                                                i3++;
                                            }
                                        }
                                        //Ecriture dans le fichier de sortie

                                        fprintf(sortie,"Case #%d: %d\n",i+1,somme);


                                    }

                            }
                                fclose(sortie);

				}
					fclose(fd);
    return 0;
}
