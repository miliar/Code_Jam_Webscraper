#include <iostream>
#include <fstream>
#include <string>
#include <math.h>

using namespace std;

int getlowest(int len, int *list) {
   int res = -1;
   for (int i = 0; i<len; i++) {
       if (list[i] >= 0) {
           if (res == -1)
               res = i;
           else if (list[i] < list[res])
               res = i;
       }
   }
   return res;
}


int work(int no, ifstream *infile, ofstream *outfile) {
   string in;
   getline(*infile,in);
   if(in.length()==0)
       return 1;
    
   int tt;
   sscanf (in.data(),"%i",&tt);

   getline(*infile,in);
   int na, nb;
   sscanf (in.data(),"%i %i", &na, &nb);

   int da[na];
   int aa[na];
   for (int i=0; i<na;i++) {
	getline(*infile,in);
        int dh, dm, ah, am;
        string temp;
        temp = in.substr(0,2);
        if (temp[0] == '0') temp = temp.substr(1,1);
        sscanf (temp.data(),"%i", &dh);
        temp = in.substr(3,2);
        if (temp[0] == '0') temp = temp.substr(1,1);
        sscanf (temp.data(),"%i", &dm);
        temp = in.substr(6,2);
        if (temp[0] == '0') temp = temp.substr(1,1);
        sscanf (temp.data(),"%i", &ah);
        temp = in.substr(9,2);
        if (temp[0] == '0') temp = temp.substr(1,1);
        sscanf (temp.data(),"%i", &am);
        da[i]=(dh*60)+dm;
        aa[i]=(ah*60)+am+tt;
   }

   int db[nb];
   int ab[nb];
   for (int i=0; i<nb;i++) {
	getline(*infile,in);
        int dh, dm, ah, am;
        string temp;
        temp = in.substr(0,2);
        if (temp[0] == '0') temp = temp.substr(1,1);
        sscanf (temp.data(),"%i", &dh);
        temp = in.substr(3,2);
        if (temp[0] == '0') temp = temp.substr(1,1);
        sscanf (temp.data(),"%i", &dm);
        temp = in.substr(6,2);
        if (temp[0] == '0') temp = temp.substr(1,1);
        sscanf (temp.data(),"%i", &ah);
        temp = in.substr(9,2);
        if (temp[0] == '0') temp = temp.substr(1,1);
        sscanf (temp.data(),"%i", &am);
        db[i]=(dh*60)+dm;
        ab[i]=(ah*60)+am+tt;
   }
   
   int resa = 0; 
   int resb = 0; 

   int low;

   while(-1<(low=getlowest(na, da)))
   {
       int dep = da[low];
       da[low]=-1;
       low = getlowest(nb, ab);
       if (-1<low) {
           if (dep<ab[low]) {
	       resa+=1;
           } else {
               ab[low] = -1;
           }
       } else {
           resa+=1;
       }
   }

   while(-1<(low=getlowest(nb, db)))
   {
       int dep = db[low];
       db[low]=-1;
       low = getlowest(na, aa);
       if (-1<low) {
           if (dep<aa[low]) {
	       resb+=1;
           } else {
               aa[low] = -1;
           }
       } else {
           resb+=1;
       }
   }

   char buffer [50];
   int n;
   sprintf (buffer, "Case #%i: %i %i\n",no,resa, resb);
   string out = buffer;
   (*outfile) <<  out ;

   return 0;
}


int main() {
   string in;
   ifstream infile;
   ofstream outfile;
   infile.open("B-large.in");
   outfile.open ("B-large.out");
   int i=0;
   getline(infile,in);
   int r=0;
   while(r==0){
       i++;
       r=work(i, &infile, &outfile);      
   }
   infile.close();
   outfile.close();
   return 0;
}
