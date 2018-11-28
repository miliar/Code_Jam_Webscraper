#include<fstream>

using namespace std;

const char* input_fname = "input";
const char* output_fname = "output";

bool Xboard[16] = {false};
bool Oboard[16] = {false};

char status = 'N';

void check(void);

int main(void)
{
    ifstream in(input_fname);
    ofstream out(output_fname);

    int testcase_sz = 0;
    in >> testcase_sz;

    for(int case_id=1;case_id<=testcase_sz;case_id++)
    {
        int num_steps = 0;
        int pos = 0;
        while(pos<16)
        {
            char sym = '.';
            in >> sym;
            switch (sym)
            {
                case 'X':
                    Xboard[pos] = true;
                    Oboard[pos++] = false;
                    num_steps++;
                    break;
                case 'O':
                    Xboard[pos] = false;
                    Oboard[pos++] = true;
                    num_steps++;
                    break;
                case 'T':
                    Xboard[pos] = true;
                    Oboard[pos++] = true;
                    num_steps++;
                    break;
                case '.':
                    Xboard[pos] = false;
                    Oboard[pos++] = false;
                    break;
                default:
                    break;
            }
        }
        if( num_steps > 15 ) status = 'D';
        else status = 'N';

        check();

        switch(status)
        {
            case 'X':
                out << "Case #" << case_id << ": X won";
                break;
            case 'O':
                out << "Case #" << case_id << ": O won";
                break;
            case 'D':
                out << "Case #" << case_id << ": Draw";
                break;
            case 'N': default:
                out << "Case #" << case_id << ": Game has not completed";
                break;
        }
        if(case_id<testcase_sz) out << endl;
    }

    return 0;
}

void check(void)
{
    if( (Xboard[0]&&Xboard[1]&&Xboard[2]&&Xboard[3]) ||
        (Xboard[4]&&Xboard[5]&&Xboard[6]&&Xboard[7]) ||
        (Xboard[8]&&Xboard[9]&&Xboard[10]&&Xboard[11]) ||
        (Xboard[12]&&Xboard[13]&&Xboard[14]&&Xboard[15]) ||
        (Xboard[0]&&Xboard[4]&&Xboard[8]&&Xboard[12]) ||
        (Xboard[1]&&Xboard[5]&&Xboard[9]&&Xboard[13]) ||
        (Xboard[2]&&Xboard[6]&&Xboard[10]&&Xboard[14]) ||
        (Xboard[3]&&Xboard[7]&&Xboard[11]&&Xboard[15]) ||
        (Xboard[0]&&Xboard[5]&&Xboard[10]&&Xboard[15]) ||
        (Xboard[3]&&Xboard[6]&&Xboard[9]&&Xboard[12]) )
    {
        status = 'X'; return;
    }
    if( (Oboard[0]&&Oboard[1]&&Oboard[2]&&Oboard[3]) ||
        (Oboard[4]&&Oboard[5]&&Oboard[6]&&Oboard[7]) ||
        (Oboard[8]&&Oboard[9]&&Oboard[10]&&Oboard[11]) ||
        (Oboard[12]&&Oboard[13]&&Oboard[14]&&Oboard[15]) ||
        (Oboard[0]&&Oboard[4]&&Oboard[8]&&Oboard[12]) ||
        (Oboard[1]&&Oboard[5]&&Oboard[9]&&Oboard[13]) ||
        (Oboard[2]&&Oboard[6]&&Oboard[10]&&Oboard[14]) ||
        (Oboard[3]&&Oboard[7]&&Oboard[11]&&Oboard[15]) ||
        (Oboard[0]&&Oboard[5]&&Oboard[10]&&Oboard[15]) ||
        (Oboard[3]&&Oboard[6]&&Oboard[9]&&Oboard[12]) )
    {
        status = 'O'; return;
    }
}
