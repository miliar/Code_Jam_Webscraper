#include<iostream>
using namespace std;
int main()
    {
        int no_cases,no_but,inp;
        char c;
        int stop_b,stop_o,prev_o,prev_b;
        int stop;
        int iter_no=0;
        cin>>no_cases;
        while(iter_no<no_cases)
            {
                cin>>no_but;
                prev_o=prev_b=stop_b=stop_o=stop=1;
                while(no_but--)
                    {
                         cin>>c;
                         cin>>inp;
                         if(c=='O')
                            {
                            //move
                                //cal num of steps
                                prev_o=prev_o-inp;
                                if(prev_o<0)
                                    prev_o=-prev_o;
                                //reach the point
                                stop_o=stop_o+prev_o;
                                prev_o=inp;
                            //press button
                                if(stop_o<=stop)
                                    {
                                        stop++;
                                        stop_o=stop;
                                    }
                                else if(stop<stop_o)
                                    {
                                        stop_o++;
                                        stop=stop_o;
                                    }
                            }
                        else if(c=='B')
                            {
                            //move
                                //cal num of steps
                                prev_b=prev_b-inp;
                                if(prev_b<0)
                                    prev_b=-prev_b;
                                //reach the point
                                stop_b=stop_b+prev_b;
                                prev_b=inp;
                            //press button
                                if(stop_b<=stop)
                                    {
                                        stop++;
                                        stop_b=stop;
                                    }
                                else if(stop<stop_b)
                                    {
                                        stop_b++;
                                        stop=stop_b;
                                    }
                            }
                    }
                    stop--;
                iter_no++;
                cout<<"Case #"<<iter_no<<": "<<stop<<endl;
            }
        return 0;
    }

