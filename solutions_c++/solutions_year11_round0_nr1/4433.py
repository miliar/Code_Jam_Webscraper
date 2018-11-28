/*
 *  Author: BK691
 */

#include <iostream>
#include <vector>
#include <utility>

using namespace std;

const int HALL_SIZE = 2;

enum Color
{
    ORANGE,
    BLUE
};

struct Button
{
    Color hall_color;
    int button_number;
    bool pressed;
    
    Button(const Color &color = (ORANGE), const int &numb = (1), const bool &pushed = (false))
        : hall_color(color), button_number(numb), pressed(pushed)
    {}

    bool operator==(const Button &rhs) const
    {
        return (hall_color == rhs.hall_color && 
                button_number == rhs.button_number && 
                pressed == rhs.pressed);
    }

    bool operator!=(const Button &rhs) const
    {
        return (hall_color != rhs.hall_color || 
                button_number != rhs.button_number || 
                pressed != rhs.pressed);
    }

    bool operator<(const Button &rhs) const
    {
        return (hall_color == rhs.hall_color && button_number < rhs.button_number);
    }

    bool operator<=(const Button &rhs) const
    {
        return (hall_color == rhs.hall_color && button_number <= rhs.button_number);
    }

    bool operator>(const Button &rhs) const
    {
        return (hall_color == rhs.hall_color && button_number > rhs.button_number);
    }

    bool operator>=(const Button &rhs) const
    {
        return (hall_color == rhs.hall_color && button_number >= rhs.button_number);
    }
 
};

struct Bot
{
    Color bot_color;
    Button* current_button;
    Button* destination_button;

    Bot(const Color &color = (ORANGE))
        : bot_color(color), current_button(NULL)
    {}

    void MoveToNextButton(Button* next_button)
    {
        current_button = next_button;
    }

    void PushButton()
    {
        if(current_button != NULL)
            current_button->pressed = true;
    }
};

struct Hallway
{
    Bot bot;
    vector< Button* > button_path;
    vector< Button* > button_sequence;
    int path_index;
    int path_dest_index;
    int seq_dest_index;
    
    Hallway(const Bot &robot = (Bot()))
        : bot(robot), path_index(0), path_dest_index(0), seq_dest_index(0)
    {}

    ~Hallway()
    {
        for(unsigned int i = 0; i < button_path.size(); ++i)
        {
            delete button_path[ i ];
            button_path[ i ] = NULL;
        }
    }

    void ConstructButtonPath(const int &max_button_number)
    {
        for(int i = 0; i < max_button_number; ++i)
            button_path.push_back( new Button(bot.bot_color, (i + 1)) );

        if(max_button_number > 0)
            bot.current_button = button_path[ path_index ];
    }

    void ObtainNextDestination()
    {
        for(unsigned int i = seq_dest_index; i < button_sequence.size(); ++i)
        {
            if(button_sequence[ i ]->hall_color == bot.bot_color)
            { 
                bot.destination_button = button_sequence[ i ];
                seq_dest_index = i + 1;
                break;
            }
        }
    }

};

int RunTestCase(vector< Button* > button_sequence, Hallway* hall);

int main()
{
    int test_cases = 0;
    int turn = 0; // turn = 1 (reading bot color), turn = 0 (reading button #)
    int button_press_number = 0;
    int button_number = 0;
    int count = 0;
    int sub_count = 0;
    int pair_count = 1;
    int orange_max_numb = 0;
    int blue_max_numb = 0;
    Color bot_color = ORANGE;
    string content = "";
    
    cin >> test_cases;
    
    int** max_button_numb = new int*[ test_cases ];
    vector< Button* >* button_sequence = new vector< Button* >[ test_cases ];

    for(int i = 0; i < test_cases; ++i)
        max_button_numb[ i ] = new int[ HALL_SIZE ];
    
    while(count < test_cases)
    {
        turn = 1;
        sub_count = 0;
        pair_count = 1;
        orange_max_numb = 0;
        blue_max_numb = 0;
        button_press_number = 0;
        
        cin >> button_press_number;

        while(sub_count < button_press_number)
        {
            if(turn)
            {
                cin >> content;

                if(content == "O")
                    bot_color = ORANGE;
                
                else if(content == "B")
                    bot_color = BLUE;
            }
            
            else
            {
                cin >> button_number;

                if(bot_color == ORANGE && button_number > orange_max_numb)
                    orange_max_numb = button_number;
                
                else if(bot_color == BLUE && button_number > blue_max_numb)
                    blue_max_numb = button_number;
                
                button_sequence[ count ].push_back( new Button(bot_color, button_number) );
            }
            
            turn = !turn;
            
            if((pair_count % 2) == 0)
                ++sub_count;
            
            ++pair_count;
        }

        max_button_numb[ count ][ ORANGE ] = orange_max_numb;
        max_button_numb[ count ][ BLUE ] = blue_max_numb;
    
        ++count;
    }

    Hallway** hall  = new Hallway*[ test_cases ];

    for(int i = 0; i < test_cases; ++i)
    {
        hall[ i ] = new Hallway[ HALL_SIZE ];

        hall[ i ][ ORANGE ] = Hallway( Bot( ORANGE ) );
        
        hall[ i ][ ORANGE ].ConstructButtonPath( max_button_numb[ i ][ ORANGE ] );

        hall[ i ][ ORANGE ].button_sequence = button_sequence[ i ];

        hall[ i ][ ORANGE ].ObtainNextDestination();

        hall[ i ][ BLUE ] = Hallway( Bot( BLUE ) );

        hall[ i ][ BLUE ].ConstructButtonPath( max_button_numb[ i ][ BLUE ] );

        hall[ i ][ BLUE ].button_sequence = button_sequence[ i ];

        hall[ i ][ BLUE ].ObtainNextDestination();
    }

    for(int i = 0; i < test_cases; ++i)
        cout << "Case #" << (i + 1) << ": " << RunTestCase( button_sequence[ i ], hall[ i ] ) << endl;
    
    // Deallocation of dynamic memory

    for(int i = 0; i < test_cases; ++i)
    {
        delete[] max_button_numb[ i ];
        delete[] hall[ i ];

        max_button_numb[ i ] = NULL;
        hall[ i ] = NULL;

        for(unsigned int index = 0; index < button_sequence[ i ].size(); ++index)
        {
            delete button_sequence[ i ][ index ];

            button_sequence[ i ][ index ] = NULL;
        }
    }

    delete[] max_button_numb;
    delete[] hall;

    max_button_numb = NULL;
    hall = NULL;
    
    return 0;
}

int RunTestCase(vector< Button* > button_sequence, Hallway* hall)
{
    if(hall != NULL)
    {        
        int total_time = 0;

        for(unsigned int i = 0; i < button_sequence.size(); ++i)
        {
            if(button_sequence[ i ] != NULL)
            {
                switch(button_sequence[ i ]->hall_color)
                {
                    case ORANGE     :   while( hall[ ORANGE ].bot.current_button->button_number != hall[ ORANGE ].bot.destination_button->button_number )
                                        {

                                            if((hall[ ORANGE ].bot.current_button->button_number - hall[ ORANGE ].bot.destination_button->button_number) > 0)
                                                --hall[ ORANGE ].path_index;

                                            else if((hall[ ORANGE ].bot.current_button->button_number - hall[ ORANGE ].bot.destination_button->button_number) < 0)
                                                ++hall[ ORANGE ].path_index;

                                            hall[ ORANGE ].bot.MoveToNextButton( hall[ ORANGE ].button_path[ hall[ ORANGE ].path_index ] );

                                            if(hall[ BLUE ].bot.current_button != NULL && hall[ BLUE ].bot.destination_button != NULL && 
                                               hall[ BLUE ].bot.current_button->button_number != hall[ BLUE ].bot.destination_button->button_number )
                                            {

                                                if((hall[ BLUE ].bot.current_button->button_number - hall[ BLUE ].bot.destination_button->button_number) > 0)
                                                    --hall[ BLUE ].path_index;

                                                else if((hall[ BLUE ].bot.current_button->button_number - hall[ BLUE ].bot.destination_button->button_number) < 0)
                                                    ++hall[ BLUE ].path_index;

                                                hall[ BLUE ].bot.MoveToNextButton( hall[ BLUE ].button_path[ hall[ BLUE ].path_index ] );
                                            }

                                            ++total_time;
                                        }

                                        hall[ ORANGE ].bot.PushButton();
                                        hall[ ORANGE ].ObtainNextDestination();

                                        if(hall[ BLUE ].bot.current_button != NULL && hall[ BLUE ].bot.destination_button != NULL && 
                                           hall[ BLUE ].bot.current_button->button_number != hall[ BLUE ].bot.destination_button->button_number )
                                        {
                                            if((hall[ BLUE ].bot.current_button->button_number - hall[ BLUE ].bot.destination_button->button_number) > 0)
                                                --hall[ BLUE ].path_index;

                                            else if((hall[ BLUE ].bot.current_button->button_number - hall[ BLUE ].bot.destination_button->button_number) < 0)
                                                ++hall[ BLUE ].path_index;

                                            hall[ BLUE ].bot.MoveToNextButton( hall[ BLUE ].button_path[ hall[ BLUE ].path_index ] );
                                        }

                                        ++total_time;

                                        break;

                    case BLUE       :   while( hall[ BLUE ].bot.current_button->button_number != hall[ BLUE ].bot.destination_button->button_number )
                                        {
                                            if((hall[ BLUE ].bot.current_button->button_number - hall[ BLUE ].bot.destination_button->button_number) > 0)
                                                --hall[ BLUE ].path_index;

                                            else if((hall[ BLUE ].bot.current_button->button_number - hall[ BLUE ].bot.destination_button->button_number) < 0)
                                                ++hall[ BLUE ].path_index;

                                            hall[ BLUE ].bot.MoveToNextButton( hall[ BLUE ].button_path[ hall[ BLUE ].path_index ] );
                                            
                                            if(hall[ ORANGE ].bot.current_button != NULL && hall[ ORANGE ].bot.destination_button != NULL && 
                                               hall[ ORANGE ].bot.current_button->button_number != hall[ ORANGE ].bot.destination_button->button_number )
                                            {
                                                if((hall[ ORANGE ].bot.current_button->button_number - hall[ ORANGE ].bot.destination_button->button_number) > 0)
                                                    --hall[ ORANGE ].path_index;

                                                else if((hall[ ORANGE ].bot.current_button->button_number - hall[ ORANGE ].bot.destination_button->button_number) < 0)
                                                    ++hall[ ORANGE ].path_index;
                                                hall[ ORANGE ].bot.MoveToNextButton( hall[ ORANGE ].button_path[ hall[ ORANGE ].path_index ] );
                                            }

                                            ++total_time;
                                        }

                                        hall[ BLUE ].bot.PushButton();
                                        hall[ BLUE ].ObtainNextDestination();
                                            
                                        if(hall[ ORANGE ].bot.current_button != NULL && hall[ ORANGE ].bot.destination_button != NULL && 
                                           hall[ ORANGE ].bot.current_button->button_number != hall[ ORANGE ].bot.destination_button->button_number )
                                        {
                                            if((hall[ ORANGE ].bot.current_button->button_number - hall[ ORANGE ].bot.destination_button->button_number) > 0)
                                                --hall[ ORANGE ].path_index;

                                            else if((hall[ ORANGE ].bot.current_button->button_number - hall[ ORANGE ].bot.destination_button->button_number) < 0)
                                                ++hall[ ORANGE ].path_index;
                                            
                                            hall[ ORANGE ].bot.MoveToNextButton( hall[ ORANGE ].button_path[ hall[ ORANGE ].path_index ] );
                                        }

                                        ++total_time;

                                        break;


                    default         :   break;
                };
            }
        }

        return total_time;
    }

    return -1;
}

