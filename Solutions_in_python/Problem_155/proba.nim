import nre
from strutils import parseInt, `%`
import optional_t

proc parseAudiance(input: string): seq[int] =
  let captures = input.match(re"^(?<aud_len>\d+) (?<aud>\d+)$").get.captures
  let aud_levels = parseInt(captures["aud_len"])
  result = newSeq[int](aud_levels + 1)
  for i, c in captures["aud"]:
    result[i] = parseInt($c)

proc sum(self: seq[int]): int =
  for v in self:
    result += v

proc simulate(self: seq[int], intialStanding=0): int =
  ## returns number still sitting
  var standing = intialStanding
  for i, v in self:
    if i <= standing:
      standing += v

  return (sum(self) + intialStanding) - standing

proc getAnswer(self: seq[int]): int =
  for i in 0..high(int):
    if simulate(self, intialStanding=i) == 0:
      return i

let testCases = parseInt(stdin.readLine())
for i in 1..testCases:
  let answer = getAnswer(parseAudiance(stdin.readLine()))
  echo("Case #$#: $#" % [$i, $answer])
