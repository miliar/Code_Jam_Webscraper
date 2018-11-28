#include <iostream>
#include <string>

class Tictactoe
{
      std::string rows[4];
public:
       void readState()
       {
            std::cin >> rows[0];
            std::cin >> rows[1];
            std::cin >> rows[2];
            std::cin >> rows[3];
       }
       void getStatus(int testid)
       {
            int xrow[4]={0,0,0,0};
            int orow[4]={0,0,0,0};
            int xcol[4]={0,0,0,0};
            int ocol[4]={0,0,0,0};
            int xdia[2]={0,0};
            int odia[2]={0,0};
            int dot = 0;
            
            for ( int rrr = 0; rrr < 4; ++rrr )
            {
                for ( int ccc = 0; ccc < 4; ++ccc )
                {
                    switch(rows[rrr][ccc])
                    {
                        case 'X':
                            ++xrow[rrr]; ++xcol[ccc]; break;
                        case 'O':
                            ++orow[rrr]; ++ocol[ccc]; break;
                        case '.':
                            ++dot; break;
                        case 'T':
                            ++xrow[rrr]; ++xcol[ccc];
                            ++orow[rrr]; ++ocol[ccc]; break;
                        default:
                            std::cout << "invalid char '" << rows[rrr][ccc] << "'"<<std::endl;
                            //exit(0);
                    }
                }
                
                switch(rows[rrr][rrr])
                {
                    case 'X':
                        ++xdia[0]; break;
                    case 'O':
                        ++odia[0]; break;
                    case '.':
                        break;
                    case 'T':
                        ++xdia[0];
                        ++odia[0]; break;
                    default:
                        std::cout << "invalid char '" << rows[rrr][rrr] << "'"<<std::endl;
                        //exit(0);
                }
                switch(rows[rrr][3-rrr])
                {
                    case 'X':
                        ++xdia[1]; break;
                    case 'O':
                        ++odia[1]; break;
                    case '.':
                        break;
                    case 'T':
                        ++xdia[1];
                        ++odia[1]; break;
                    default:
                        std::cout << "invalid char '" << rows[rrr][3-rrr] << "'"<<std::endl;
                        //exit(0);
                }
            }
            
            std::string result=dot?"Game has not completed":"Draw";
            if ( 4 == xrow[0] || 4 == xrow[1] || 4 == xrow[2] || 4 == xrow[3] || 
                 4 == xcol[0] || 4 == xcol[1] || 4 == xcol[2] || 4 == xcol[3] || 
                 4 == xdia[0] || 4 == xdia[1] )
                 result = "X won";
            if ( 4 == orow[0] || 4 == orow[1] || 4 == orow[2] || 4 == orow[3] || 
                 4 == ocol[0] || 4 == ocol[1] || 4 == ocol[2] || 4 == ocol[3] || 
                 4 == odia[0] || 4 == odia[1] )
                 result = "O won";
            
            std::cout << "Case #" << testid << ": " << result << std::endl; 
       }
};

int main()
{
    Tictactoe solver;
    int testcases;
    std::cin >> testcases;
    
    for(int iii = 1; iii <= testcases; ++iii)
    {
        solver.readState();
        solver.getStatus(iii);
    }
        
    return 0;
}
