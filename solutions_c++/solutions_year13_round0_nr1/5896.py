#include<iostream>
using namespace std;
 void print(int kapil)
{ switch(kapil)
     {case 1:cout<<"O won";
                        break;
                case 2:cout<<"X won";
                        break;
                case 3:cout<<"Draw";
                break;
                case 4: cout<<"Game has not completed";
     }
     cout<<"\n";
}
int main()
{int de,ef,eff,fgg,fg,m;
    char bd[10][10];
   cin>>de;
    m=de;
    while(de--)
    {cout<<"Case #"<<m-de<<": ";
              for(ef=0;ef<4;ef++)
            cin>>bd[ef];
             int cid,fid,iim,kapil;
              cid=fid=iim=kapil=0;
          for(ef=0;ef<4;ef++)
              { cid=fid=iim=0;
                 for(fg=0;fg<4;fg++)
                              {               if(bd[ef][fg]=='X')
                                              fid++;
                                             if(bd[ef][fg]=='T')
                                              iim++;
		 if(bd[ef][fg]=='O')
                                              cid++;
                                 } if(fid+iim==4)
                              kapil=2;       
                      if(cid+iim==4)
                              kapil=1;
                    }
              if(kapil)
       { print(kapil);
                     continue;
              }for(fgg=0;fgg<4;fgg++)
         {cid=fid=iim=0;
           for(ef=0;ef<4;ef++)
                              {  if(bd[ef][fgg]=='X')
                                              fid++;
                                             if(bd[ef][fgg]=='T')
                                              iim++;
		 if(bd[ef][fgg]=='O')
                                              cid++;
                              }if(fid+iim==4)
                              kapil=2;                             
                             if(cid+iim==4)
                              kapil=1;
                      }if(kapil)
              {
                     print(kapil);
                     continue;
              } cid=fid=iim=0;
              for(ef=0;ef<4;ef++)
                          { if(bd[ef][ef]=='X')
                                              fid++;
                                             if(bd[ef][ef]=='T')
                                              iim++;
		 if(bd[ef][ef]=='O')
                                              cid++;
                     }if(fid+iim==4)
                              kapil=2;
if(cid+iim==4)
                              kapil=1;
                         if(kapil)
                              {
                     print(kapil);
                     continue;
                              }
                           cid=fid=iim=0;
              for(ef=0;ef<4;ef++)
                              {
                                               if(bd[3-ef][ef]=='O')
                                              cid++;
                                              if(bd[3-ef][ef]=='X')
                                              fid++;
                                              if(bd[3-ef][ef]=='T')
                                              iim++;
                              } if(fid+iim==4)
                              kapil=2;     
                              if(cid+iim==4)
                              kapil=1;
                              if(kapil)
                              {
                     print(kapil);
                     continue;
                              }
              int ab=0;
              for(eff=0;eff<4;eff++)
              for(fg=0;fg<4;fg++)
              if(bd[eff][fg]=='O'||bd[eff][fg]=='X'||bd[eff][fg]=='T')
              ab++;                
              
              if(ab==16)kapil=3;
              else kapil=4;       
	print(kapil);         
              }
              return 0;
    } 
              
              
              
              
              
