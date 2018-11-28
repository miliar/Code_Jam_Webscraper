#include <iostream.h>
#include <sstream>

struct Snapper
{
    public:
        bool state;
        bool power;
};

int main()
{
    int noOfTestCases = 0;
    int noOfSnappers =  0;
    int snaps = 0;
    freopen ("input.txt", "rt", stdin);
    freopen ("output.txt", "wt", stdout);

    cin >> noOfTestCases;

    for (int i=0; i < noOfTestCases; i++)
    {
        cout << "Case #" << i+1 << ": ";
        cin >> noOfSnappers;
        cin >> snaps;
        
        Snapper *snapper = new Snapper[noOfSnappers];

        //initialize the snappers
        snapper[0].power = true;
        snapper[0].state = false;
        for (int j=1; j<noOfSnappers; j++)
        {
            snapper[j].state = false;
            snapper[j].power = false;
        }

        //Lets run through the snaps
        for (int k=0; k<snaps; k++)
        {
            //for each snap change the state of the snappers
            for (int j=0; j < noOfSnappers; j++)
            {
                if (snapper[j].power == true) //if the snapper is getting power
                    snapper[j].state = !(snapper[j].state);
                
                if (j!=0)
                {
                    if (snapper[j-1].state == true && snapper[j-1].power == true)
                        snapper[j].power = true;
                    else
                        snapper[j].power = false;
                }
                
            }
        }

        //Now check the current state
        int bulb = true;
        for (int j=0; j<noOfSnappers; j++)
        {
            if (snapper[j].state == true && snapper[j].power == true && bulb == true)
                bulb = true;
            else
                bulb = false;
        }

        if (bulb)
            cout << "ON" << endl;
        else
            cout << "OFF" << endl;

        delete [] snapper;
    }
}


// vim:ts=4:sw=4:expandtab:ai:cindent
