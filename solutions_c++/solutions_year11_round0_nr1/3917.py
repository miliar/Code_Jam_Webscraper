/* 
 * File:   main.cpp
 * Author: rigved
 *
 * Created on 7 May, 2011, 12:44 PM
 */

#include <stdlib.h>
#include <iostream>

/*
 * 
 */
int main(int argc, char** argv)
{
    int T, N, last_position[2], from, to, difference, moves_to_complete_of_earlier, moves_to_complete, total_moves;
    char earlier_robot, current_robot;
    
    std::cin>>T;

    for (int i=1; i<=T; i++)
        {
            std::cin>>N;

            last_position[0]=last_position[1]=1;

            moves_to_complete_of_earlier=total_moves=0;

            for (int j=1; j<=N; j++)
                {
                    std::cin>>current_robot;

                    if (j==1)
                        earlier_robot=current_robot;

                    if ((current_robot=='O') || (current_robot=='o'))
                        from=last_position[0];
                    else
                        from=last_position[1];

                    std::cin>>to;

                    difference=abs(from-to);

                    if (earlier_robot!=current_robot)
                        {
                            if (difference>moves_to_complete_of_earlier)
                                difference-=moves_to_complete_of_earlier;
                            else
                                difference=0;
                        }
                    moves_to_complete=difference+1;

                    total_moves+=moves_to_complete;

                    if (earlier_robot==current_robot)
                        moves_to_complete_of_earlier+=moves_to_complete;
                    else
                        moves_to_complete_of_earlier=moves_to_complete;

                    if ((current_robot=='O') || (current_robot=='o'))
                        last_position[0]=to;
                    else
                        last_position[1]=to;
                    earlier_robot=current_robot;
                }

            std::cout<<"Case #"<<i<<": "<<total_moves<<std::endl;
        }
    return (EXIT_SUCCESS);
}
