#include <iomanip>
#include <iostream>
#include <vector>

typedef std::vector<bool> BoolVector;
typedef std::vector<BoolVector> BoolMatrix;
typedef long double Real;
typedef std::vector<Real> RealVector;


struct TournamentSchedule {
    size_t number_of_teams;
    BoolMatrix is_played;
    BoolMatrix is_won;
};


TournamentSchedule Input(std::istream* istream)
{
    size_t number_of_teams;
    (*istream) >> number_of_teams;

    TournamentSchedule result;
    result.number_of_teams = number_of_teams;
    result.is_played.resize(number_of_teams, BoolVector(number_of_teams, false));
    result.is_won.resize(number_of_teams, BoolVector(number_of_teams, false));

    for (size_t team_offset = 0; team_offset < number_of_teams; ++team_offset) {
        std::string team_line;
        (*istream) >> team_line;

        for (size_t opponent_offset = 0; opponent_offset < number_of_teams; ++opponent_offset) {
            if (team_line.at(opponent_offset) == '1') {
                result.is_played[team_offset][opponent_offset] = true;
                result.is_won[team_offset][opponent_offset] = true;
            } else if (team_line.at(opponent_offset) == '0') {
                result.is_played[team_offset][opponent_offset] = true;
                result.is_won[team_offset][opponent_offset] = false;                
            }
        }
    }

    return result;
}


RealVector EvaluateRatingsPercentageIndex(const TournamentSchedule& tournament_schedule)
{
/*
    for (size_t i = 0; i < tournament_schedule.number_of_teams; ++i) {
        for (size_t j = 0; j < tournament_schedule.number_of_teams; ++j) {
            std::cerr << (tournament_schedule.is_played[i][j] ? (
                              tournament_schedule.is_won[i][j] ? 
                              '1' : '0') : '.'); 
        }
        std::cerr << '\n';
    }
*/

    RealVector number_of_plays(tournament_schedule.number_of_teams, 0);
    RealVector number_of_wins(tournament_schedule.number_of_teams, 0);

    for (size_t team_offset = 0; team_offset < tournament_schedule.number_of_teams; ++team_offset) {
        for (size_t opponent_offset = 0; opponent_offset < tournament_schedule.number_of_teams; ++opponent_offset) {
            if (tournament_schedule.is_played[team_offset][opponent_offset]) {
                ++number_of_plays[team_offset];
            }
            if (tournament_schedule.is_won[team_offset][opponent_offset]) {
                ++number_of_wins[team_offset];
            }
        }
    }

    RealVector wp(tournament_schedule.number_of_teams, 0);
    for (size_t team_offset = 0; team_offset < tournament_schedule.number_of_teams; ++team_offset) {
        wp[team_offset] = number_of_wins[team_offset] / number_of_plays[team_offset];
    }

    RealVector owp(tournament_schedule.number_of_teams, 0);
    for (size_t team_offset = 0; team_offset < tournament_schedule.number_of_teams; ++team_offset) {
        for (size_t opponent_offset = 0; opponent_offset < tournament_schedule.number_of_teams; ++opponent_offset) {
            if (!tournament_schedule.is_played[team_offset][opponent_offset]) {
                continue;
            }
            if (tournament_schedule.is_won[team_offset][opponent_offset]) {
                owp[team_offset] += number_of_wins[opponent_offset] / (number_of_plays[opponent_offset] - 1);
            } else {
                owp[team_offset] += (number_of_wins[opponent_offset] - 1) / (number_of_plays[opponent_offset] - 1);
            }
        }
        owp[team_offset] /= number_of_plays[team_offset];
    }

    RealVector oowp(tournament_schedule.number_of_teams, 0);
    for (size_t team_offset = 0; team_offset < tournament_schedule.number_of_teams; ++team_offset) {        
        for (size_t opponent_offset = 0; opponent_offset < tournament_schedule.number_of_teams; ++opponent_offset) {
            if (!tournament_schedule.is_played[team_offset][opponent_offset]) {
                continue;
            }
            oowp[team_offset] += owp[opponent_offset];
        }

        oowp[team_offset] /= number_of_plays[team_offset];
    }

    RealVector result;
    for (size_t team_offset = 0; team_offset < tournament_schedule.number_of_teams; ++team_offset) {
        result.push_back(wp[team_offset] / 4 + owp[team_offset] / 2 + oowp[team_offset] / 4);
    }

    return result;
}


int main()
{
    size_t number_of_test_cases;
    std::cin >> number_of_test_cases;

    for (size_t case_index = 1; case_index <= number_of_test_cases; ++case_index) {
        TournamentSchedule tournament_schedule = Input(&std::cin);

        std::cout << "Case #" << case_index << ":\n";
        const RealVector result = EvaluateRatingsPercentageIndex(tournament_schedule);
        for (size_t i = 0; i < result.size(); ++i) {
            std::cout << std::setprecision(8) << result[i] << '\n';
        }
    }

    return 0;
}

