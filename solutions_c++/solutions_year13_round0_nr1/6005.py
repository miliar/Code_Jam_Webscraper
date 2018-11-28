#include <iostream>
#include <fstream>


using namespace std;


int main()

{

    char a[4][4],hl,win='D';

    int i,j,k,T;

    int d=0,f=1,complete=0;
	ifstream in("A-large.in");
	ofstream out("new.txt");

    

    in >> T;

    

    for (k=1; k<=T; k++)

    {

        win='D';

        d=0;

        f=1;

        complete=0;

        

        for (i=0;i<4;i++)

        {

            for (j=0;j<4;j++)

            {

                a[i][j]='.';

            }

        }

        

        for (i=0;i<4;i++)

        {

            d=0;

            f=1;

            for (j=0;j<4;j++)

            {

                in >> a[i][j];

                if (d==0)

                {

                    if (a[i][j]!='T')

                    {

                        hl=a[i][j];

                        d=1;

                    }

                }

                else //(d==1)

                {

                    if(hl!=a[i][j] && a[i][j]!='T')

                    {

                        f=0;

                    }

                }

                

            }

            

            if(f==1 && complete == 0)

            {

                win=hl;

                if(win!='.')

                {

                    complete = 1;

                }

            }

            

        }

        

        

        if (complete==0)

        {

            

            for (i=0;i<4;i++)

            {

                d=0;

                f=1;

                for (j=0;j<4;j++)

                {

                    if (d==0)

                    {

                        if (a[j][i]!='T')

                        {

                            hl=a[j][i];

                            d=1;

                        }

                    }

                    else //(d==1)

                    {

                        if(hl!=a[j][i] && a[j][i]!='T')

                        {

                            f=0;

                        }

                    }

                    

                }

                

                if(f==1 && complete == 0)

                {

                    win=hl;

                    if(win!='.')

                    {

                        complete = 1;

                    }

                }

                

            }

            

        }

        

        

        if (complete==0)

        {

            d=0;

            f=1;

            for (i=0,j=0 ; i<4 && j<4; i++,j++)

            {

                

                if (d==0)

                {

                    if (a[i][j]!='T')

                    {

                        hl=a[i][j];

                        d=1;

                    }

                }

                else //(d==1)

                {

                    if(hl!=a[i][j] && a[i][j]!='T')

                    {

                        f=0;

                    }

                }

                

            }

            

            if(f==1 && complete == 0)

            {

                win=hl;

                if(win!='.')

                {

                    complete = 1;

                }

            }

            

        }

        

        

        

        if (complete==0)

        {

            d=0;

            f=1;

            for (i=3,j=0 ; i>=0 && j<4; i--,j++)

            {

                

                if (d==0)

                {

                    if (a[i][j]!='T')

                    {

                        hl=a[i][j];

                        d=1;

                    }

                }

                else //(d==1)

                {

                    if(hl!=a[i][j] && a[i][j]!='T')

                    {

                        f=0;

                    }

                }

                

            }

            

            if(f==1 && complete == 0)

            {

                win=hl;

                if(win!='.')

                {

                    complete = 1;

                }

            }

            

        }

        
		if(win=='D')
       {
           f=0;
           for (i=0;i<4;i++)
           {
               for (j=0;j<4;j++)
               {
                   if (a[i][j]=='.')
                       f=1;
               }
           }
           
           if(f==1)
           {
               win='.';
           }
       }
        


        switch (win)

        {

            case 'X' : out << "Case #" << k <<": X won"<<"\n" ;

                break;

                

            case 'O' : out << "Case #" << k <<": O won"<<"\n" ;

                break;

                

            case 'D' : out << "Case #" << k <<": Draw"<<"\n" ;

                break;

                

            case '.' : out << "Case #" << k <<": Game has not completed"<<"\n" ;

                break;

        }

    }


    return 0;

}