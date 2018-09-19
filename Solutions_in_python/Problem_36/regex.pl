sub match_all_ways {
    my ($string, $regex) = @_;
    my $count;
    my $incr = qr/(?{$count++})/;
    $string =~ /(?:$regex)$incr(?!)/;
    return $count;
}
print match_all_ways($ARGV[0], qr/w.*e.*l.*c.*o.*m.*e.* .*t.*o.* .*c.*o.*d.*e.* .*j.*a.*m/);
