# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 17:52:39 2014

@author: Baplar
"""

# Convert input file into a list
with open("Input.txt","r") as fichier_entree:
    entree=fichier_entree.read()
liste_entree=entree.split("\n")

liste_sortie=[]

for i, chain in enumerate(liste_entree):
    if i==0:
        # Extract T
        liste_entree[0]=T=int(chain)
    if 0<i<T+1:
        # Transform each chain of the list into a list of parameters (R, C, M)
        liste_entree[i]=chain.split(" ")
        
        # Extract parameters
        R=int(liste_entree[i][0])
        C=int(liste_entree[i][1])
        M=int(liste_entree[i][2])
        
        chaine=""
        
        # Ugly case disjunction, based on prior home-made research
        
        if R>=3 and C>=3:
            if (R*C)-M in [2,3,5,7]:
                liste_sortie.append("Impossible")
            
            elif R*C-M>=2*C+2:
                chaine="c"+(C-1)*"."
                if M%C==C-1:
                    chaine+=(R-3-M//C)*("\n"+C*".")+"\n"+(C-1)*"."+"*\n.."\
                    +(C-2)*"*"+(M//C)*("\n"+C*"*")
                
                elif M%C==0:
                    chaine+=(R-1-M//C)*("\n"+C*".")+(M//C)*("\n"+C*"*")
                
                else:
                    chaine+=(R-2-M//C)*("\n"+C*".")+"\n"+(C-M%C)*"."\
                    +M%C*"*"+(M//C)*("\n"+C*"*")
                liste_sortie.append(chaine)

            elif R*C-M>=8:
                col=(M-(R-3)*C)
                if col%3==0:
                    col=col//3
                    chaine="c"+(C-1-col)*"."+col*"*"\
                    +2*("\n"+(C-col)*"."+col*"*")+(R-3)*("\n"+C*"*")
                elif col%3==1:
                    col=(col-1)//3
                    chaine="c"+(C-1-col)*"."+col*"*"+"\n"+(C-col)*"."+col*"*"\
                    +"\n"+(C-1-col)*"."+(col+1)*"*"+(R-3)*("\n"+C*"*")
                elif col%3==2:
                    col=(col-2)//3
                    chaine="c"+(C-1-col)*"."+col*"*"+"\n"+(C-col)*"."+col*"*"\
                    +"\n"+(C-2-col)*"."+(col+2)*"*"+(R-3)*("\n"+C*"*")
                liste_sortie.append(chaine)
            
            elif R*C-M==6 or R*C-M==4:
                col=(R*C-M)//2
                chaine="c"+(col-1)*"."+(C-col)*"*"+"\n"+col*"."+(C-col)*"*"\
                +(R-2)*("\n"+C*"*")
                liste_sortie.append(chaine)
            
            elif R*C-M==1:
                chaine="c"+(C-1)*"*"+(R-1)*("\n"+C*"*")
                liste_sortie.append(chaine)
        
        elif R==2 and C>2:
            if (M%2==1 and M!=R*C-1) or M==R*C-2:
                liste_sortie.append("Impossible")
            
            elif M==R*C-1:
                chaine="c"+(C-1)*"*"+"\n"+C*"*"
                liste_sortie.append(chaine)
            
            else:
                col=M//2
                chaine="c"+(C-1-col)*"."+col*"*"+"\n"+(C-col)*"."+col*"*"
                liste_sortie.append(chaine)
        
        elif C==2 and R>2:
            if (M%2==1 and M!=R*C-1) or M==R*C-2:
                liste_sortie.append("Impossible")
            
            elif M==R*C-1:
                chaine="c*"+(R-1)*"\n**"
                liste_sortie.append(chaine)
            
            else:
                lig=M//2
                chaine="c."+(R-1-lig)*"\n.."+lig*"\n**"
                liste_sortie.append(chaine)
        
        elif C==R==2:
            if M==1 or M==2:
                liste_sortie.append("Impossible")
            elif M==0:
                liste_sortie.append("c.\n..")
            elif M==3:
                liste_sortie.append("c*\n**")
        
        elif C==1:
            chaine="c"+(R-1-M)*"\n."+M*"\n*"
            liste_sortie.append(chaine)
        
        elif R==1:
            chaine="c"+(C-1-M)*"."+M*"*"
            liste_sortie.append(chaine)
        
        else:
            liste_sortie.append("Dafuq just happened ?")
        
# Output in a file        
        
with open("Output.txt", "w") as fichier_sortie:
    for pos, sortie in enumerate(liste_sortie):
        chaine_sortie="Case #" + str(pos+1) + ":\n" +sortie # Concatenate chain
        if pos+1==T:
            # To not leave a blank line at the end of the file
            fichier_sortie.write(chaine_sortie)
        else:
            fichier_sortie.write(chaine_sortie + "\n")