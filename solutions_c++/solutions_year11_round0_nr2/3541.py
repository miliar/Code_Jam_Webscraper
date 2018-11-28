/* 
 * File:   main.cpp
 * Author: rigved
 *
 * Created on 7 May, 2011, 5:53 PM
 */

#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

/*
 * 
 */
int main(int argc, char** argv)
{
    int T, C, D, N;

    std::cin>>T;

    for (int i=1; i<=T; i++)
        {
            std::cin>>C;

            std::string invocation_list[C];

            for (int j=0; j<C; j++)
                std::cin>>invocation_list[j];

            std::cin>>D;

            std::string revocation_list[D];

            for (int j=0; j<D; j++)
                std::cin>>revocation_list[j];

            std::cin>>N;

            std::string input;

            std::cin>>input;
            
            std::vector<char> final_list;

            for (int j=0; j<N; j++)
                {
                    if (final_list.empty())
                        {
                            final_list.push_back(input.at(j));
                        }
                    else
                        {
                            bool flag=false;

                            for (int k=0; ((k<C) && (!flag)); k++)
                                {
                                    if ((input.at(j)==invocation_list[k].at(0)) && (invocation_list[k].at(1)==final_list.back()))
                                        {
                                            final_list.pop_back();
                                            final_list.push_back(invocation_list[k].at(2));
                                            flag=true;
                                            break;
                                        }
                                    else if ((input.at(j)==invocation_list[k].at(1)) && (invocation_list[k].at(0)==final_list.back()))
                                            {
                                                final_list.pop_back();
                                                final_list.push_back(invocation_list[k].at(2));
                                                flag=true;
                                                break;
                                            }
                                }

                            for (int k=0; ((k<D) && (!flag)); k++)
                                {
                                    if ((input.at(j)==revocation_list[k].at(0)) && ((std::find(final_list.begin(), final_list.end(), revocation_list[k].at(1))!=final_list.end()) || revocation_list[k].at(1)==final_list.back()))
                                        {
                                            final_list.clear();
                                            flag=true;
                                            break;
                                        }
                                    else if ((input.at(j)==revocation_list[k].at(1)) && ((std::find(final_list.begin(), final_list.end(), revocation_list[k].at(0))!=final_list.end()) || revocation_list[k].at(0)==final_list.back()))
                                            {
                                                final_list.clear();
                                                flag=true;
                                                break;
                                            }
                                }

                            if (!flag)
                                final_list.push_back(input.at(j));
                        }
                }

            std::cout<<"Case #"<<i<<": [";
            if (!final_list.empty())
                std::cout<<final_list.front();
            for (unsigned int j=1; j<final_list.size(); j++)
                std::cout<<", "<<final_list.at(j);
            std::cout<<"]"<<std::endl;
        }
    return (EXIT_SUCCESS);
}
