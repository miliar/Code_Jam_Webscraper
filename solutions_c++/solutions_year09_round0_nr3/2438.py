#include <cstdlib>
#include <iostream>
#include <string>

using namespace std;

int n=0,i,j;

string parrafo="";
string w="welcome to code jam";

long int cuenta(string s){
     long int n=0;
     long int l=s.size();
     //cout << l << endl;
     for(  int i01=0      ;  i01<(l-18)  ;  i01++  )
     for(  int i02=i01+1  ;  i02<(l-17)  ;  i02++  )
     for(  int i03=i02+1  ;  i03<(l-16)  ;  i03++  )
     for(  int i04=i03+1  ;  i04<(l-15)  ;  i04++  )
     for(  int i05=i04+1  ;  i05<(l-14)  ;  i05++  )
     for(  int i06=i05+1  ;  i06<(l-13)  ;  i06++  )
     for(  int i07=i06+1  ;  i07<(l-12)  ;  i07++  )
     for(  int i08=i07+1  ;  i08<(l-11)  ;  i08++  )
     for(  int i09=i08+1  ;  i09<(l-10)  ;  i09++  )
     for(  int i10=i09+1  ;  i10<(l- 9)  ;  i10++  )
     for(  int i11=i10+1  ;  i11<(l- 8)  ;  i11++  )
     for(  int i12=i11+1  ;  i12<(l- 7)  ;  i12++  )
     for(  int i13=i12+1  ;  i13<(l- 6)  ;  i13++  )
     for(  int i14=i13+1  ;  i14<(l- 5)  ;  i14++  )
     for(  int i15=i14+1  ;  i15<(l- 4)  ;  i15++  )
     for(  int i16=i15+1  ;  i16<(l- 3)  ;  i16++  )
     for(  int i17=i16+1  ;  i17<(l- 2)  ;  i17++  )
     for(  int i18=i17+1  ;  i18<(l- 1)  ;  i18++  )
     for(  int i19=i18+1  ;  i19<(l   )  ;  i19++  )
       if(
          s[i01]=='w' && 
          s[i02]=='e' && 
          s[i03]=='l' && 
          s[i04]=='c' && 
          s[i05]=='o' && 
          s[i06]=='m' && 
          s[i07]=='e' && 
          s[i08]==' ' && 
          s[i09]=='t' && 
          s[i10]=='o' && 
          s[i11]==' ' && 
          s[i12]=='c' && 
          s[i13]=='o' && 
          s[i14]=='d' && 
          s[i15]=='e' && 
          s[i16]==' ' && 
          s[i17]=='j' && 
          s[i18]=='a' && 
          s[i19]=='m' ){
          n++;
          /*
          cout << nespacios(i01) << 
                  s[i01] << nespacios(i02-i01-1) <<
                  s[i02] << nespacios(i03-i02-1) <<
                  s[i03] << nespacios(i04-i03-1) <<
                  s[i04] << nespacios(i05-i04-1) <<
                  s[i05] << nespacios(i06-i05-1) <<
                  s[i06] << nespacios(i07-i06-1) <<
                  s[i07] << nespacios(i08-i07-1) <<
                  s[i08] << nespacios(i09-i08-1) <<
                  s[i09] << nespacios(i10-i09-1) <<
                  s[i10] << nespacios(i11-i10-1) <<
                  s[i11] << nespacios(i12-i11-1) <<
                  s[i12] << nespacios(i13-i12-1) <<
                  s[i13] << nespacios(i14-i13-1) <<
                  s[i14] << nespacios(i15-i14-1) <<
                  s[i15] << nespacios(i16-i15-1) <<
                  s[i16] << nespacios(i17-i16-1) <<
                  s[i17] << nespacios(i18-i17-1) <<
                  s[i18] << nespacios(i19-i18-1) <<
                  s[i19] << 
                  endl;                  
          */
          /*
          cout << i01 << "\t" <<
                  i02 << "\t" <<
                  i03 << "\t" <<
                  i04 << "\t" <<
                  i05 << "\t" <<
                  i06 << "\t" <<
                  i07 << "\t" <<
                  i08 << "\t" <<
                  i09 << "\t" <<
                  i10 << "\t" <<
                  i11 << "\t" <<
                  i12 << "\t" <<
                  i13 << "\t" <<
                  i14 << "\t" <<
                  i15 << "\t" <<
                  i16 << "\t" <<
                  i17 << "\t" <<
                  i18 << "\t" <<
                  i19 << "\t" <<
                  endl;
           */   
          }
          
     
     return n;
}

string nespacios(int n){
    string sal="";
    for(int i=0;i<n;i++)
      sal+=" ";
    return sal;
}

string conformato(long int n){
    string s="";
    
    s+=( '0'+(n/1000)%10 );
    s+=( '0'+(n/100 )%10 );
    s+=( '0'+(n/10  )%10 );
    s+=( '0'+(n     )%10 );
    return s;
}

int main(int argc, char *argv[])
{
    cin >> n;
    
    //cin.ignore(,);
    
    getline(cin,parrafo);
    
    for(i=0;i<n;i++){
      getline(cin,parrafo);
      
      cout << "Case #" << (i+1) <<": " << conformato(cuenta(parrafo)) << endl;
    }
    
    
    //system("PAUSE");
    return EXIT_SUCCESS;
}
