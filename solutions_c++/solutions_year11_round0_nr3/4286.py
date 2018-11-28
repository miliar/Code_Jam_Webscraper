
/*
 * main.cc
 *
 *  Created on: Dec 12, 2009
 *      Author: Qian Xin
 *      DataStructure Java book 11.2.2
 */

#include "xinqian.h"

int debug_level = 0;

int main()
{
    TestCase *the_case;
    fstream in_file;
    int case_count;
    int failed=0;

    //in_file.open ("C-large.in", fstream::in);

    istream& in=cin;

    in>>case_count;
    if (case_count<=0)
    {
        cerr<<"invalid case_count"<<case_count;
        failed=1;
        return 0;
    }

    for (int i = 1; i <= case_count; i++)
    {
        debug_print("case:"<<i<<"======================="<<endl);
        the_case = new TestCase();
        the_case->input(in);
        if (!the_case->getPossible())
            {
                cout<<"Case #"<<i<<": NO"<<endl;
            }
        else
        {
            cout<<"Case #"<<i<<": "<<the_case->sum-the_case->min<<endl;
        }

        delete the_case;
    }
    return 0;
}

