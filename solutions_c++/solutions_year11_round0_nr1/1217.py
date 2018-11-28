//
//  main.cpp
//  Friendly_robots
//
//  Created by Edouard Richard on 07/05/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <stdlib.h> 

using namespace std;

struct operation {
    char robot;
    int button;
};

int GetIntVal(string strConvert) {
    int intReturn;
    
    // NOTE: You should probably do some checks to ensure that
    // this string contains only numbers. If the string is not
    // a valid integer, zero will be returned.
    intReturn = atoi(strConvert.c_str());
    
    return(intReturn); 
}

int Split(vector<string>& vecteur, string chaine, char separateur)
{
    vecteur.clear();
    string::size_type stTemp = chaine.find(separateur);
    while(stTemp != string::npos)
    {
        vecteur.push_back(chaine.substr(0, stTemp));
        chaine = chaine.substr(stTemp + 1);
        stTemp = chaine.find(separateur);
    }
    vecteur.push_back(chaine);
    return vecteur.size();
} 

int getNextOperation(vector<operation> sequence, char robot, int operationActuelle) {
    for (int i=operationActuelle+1; i < sequence.size(); i++) {
        if (sequence[i].robot == robot) {
            return i;
        }
    }
    return NULL;
}

int main (int argc, const char * argv[])
{
    
    int nbCase;
    
    

    
    ifstream fichier(argv[1], ios::in);  // on ouvre le fichier en lecture
    
    if(fichier)  // si l'ouverture a réussi
    {       
        
        string ligne;
        int l=0;
        while(getline(fichier, ligne))  // tant que l'on peut mettre la ligne dans "contenu"
        {
            if (l==0) {
                nbCase = GetIntVal(ligne);
                
            } else {
                


                
                
                
                vector<string> VecStr;
                int nbElement = Split(VecStr, ligne, ' ');
                
                vector<operation> sequence;
                
                // création de la séquence
                for(int i = 1; i < nbElement-1; i=i+2)
                {
                    operation o;
                    o.robot = VecStr[i][0];
                    o.button = GetIntVal(VecStr[i+1]);
                    sequence.push_back(o);
                } 
                
                
                // OPERATION
                
                int couloirO = 1;
                int couloirB= 1;
                int time = 0;
                
                int operation=0, nvle_operation = 0;
                
                int operationB = getNextOperation(sequence, 'B', -1);

                int operationO = getNextOperation(sequence, 'O', -1);
                
                

                while (sequence.size() > operation) {  
                    nvle_operation = operation;
                    time++;

                    
                    
                    // les deux robots sont sur leurs bouttons
                    if ((sequence[operationB].button == couloirB) && (sequence[operationO].button == couloirO)) {
                        
                        if (sequence[operation].robot == 'B') {

                            operationB = getNextOperation(sequence, 'B', operation);

                            nvle_operation++;
                            
                        } else {
                        operationO = getNextOperation(sequence, 'O', operation);
                        nvle_operation++;
                        }
                        
                    } else {
                        
//                        if (((sequence[operation].robot == 'O') && (sequence[operationO].button == couloirO)) {
//                            
//                        } else if ((sequence[operation].robot == 'B') && (sequence[operationB].button == couloirB))) {
//                            
//                        }
                        
                        // ORANGE
                        // le robot est sur sa case
                        if (sequence[operationO].button == couloirO) {
                            //si c'est à lui,  il appuie
                            if (sequence[operation].robot == 'O') {

                                operationO = getNextOperation(sequence, 'O', operation);
                                nvle_operation++;
                            }
                            
                            // il doit se déplacer
                        } else if (sequence[operationO].button > couloirO) {
                            couloirO++;

                        } else {
                            couloirO--;

                        }
                        
                        
                        // BLEU
                        // le robot est sur sa case
                        if (sequence[operationB].button == couloirB) {
                            //si c'est à lui,  il appuie
                            if (sequence[operation].robot == 'B') {

                                operationB = getNextOperation(sequence, 'B', operation);
                                nvle_operation++;

                            }
                            
                            // il doit se déplacer
                        } else if (sequence[operationB].button > couloirB) {
                            couloirB++;

                        } else {
                            couloirB--;

                        }
                        
                        
                        
                        
                    }
                    operation = nvle_operation;
                    
//                    if (sequence[operation].robot == 'B')  {
//                        cout << "robot bleu doit appuyer sur button " << sequence[operation].button << endl;
//                        if (sequence[operation].button == couloirB) {
//                            cout << "bleu appuie sur le boutton "<< sequence[operation].button<<endl; 
//                            operation++;
//                            
//                        } else if (sequence[operation].button > couloirB) {
//                            couloirB++;
//                        } else {
//                            couloirB--;
//                        }
//                    }

                    

                }
                

                cout << "Case #" << l << ": " << time << endl;
                
            }
            
            l++;
        }
        fichier.close();  // on ferme le fichier
    }
    else  // sinon
        cerr << "Impossible d'ouvrir le fichier !" << endl;
    
    
    
 
    
    return 0;
}

